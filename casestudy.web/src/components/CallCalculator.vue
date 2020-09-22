<template>
  <div>
    <v-form @submit.prevent="calculate">
      <v-card-text>
        <v-menu
          v-model="date_menu"
          max-width="290px"
          min-width="290px"
        >
          <template v-slot:activator="{ on }">
            <v-text-field v-on="on"
              label="Date"
              v-model="date"
              :required=true
            ></v-text-field>
          </template>
          <v-date-picker
            locale="en-in"
            v-model="date"
            no-title
            @input="date_menu=false"
          ></v-date-picker>
        </v-menu>
      </v-card-text>
      <v-select
        v-model=rule
        label="Rules"
        :items="rules"
        item-text="text"
        item-value="value"
      ></v-select>
      <v-text-field
        v-model="investment_name"
        label="Investment Name"
        :required=true
      ></v-text-field>
      <v-text-field
        v-model="investment_requirement"
        label="Capital Required for Investment"
        type="number"
        :required=true
      ></v-text-field>
      <v-btn color="primary" class="mr-3" type="submit">Calculate</v-btn>
    </v-form>
    <v-data-table
      :items="fundcommitments"
      :headers="fundcommitmentheaders"
      hide-default-footer
    ></v-data-table>
    <v-data-table
      :items="funds"
      :headers="fundsheaders"
      hide-default-footer
    ></v-data-table>
    <v-btn color="primary" class="mr-3" type="button" :disabled="confirm_disabled" @click="confirm">Confirm</v-btn>
  </div>
</template>

<script>
export default {
  data() {
    return {
      confirm_disabled: true,
      date_menu: false,
      date: '',
      rules: [{text: 'First In First Out (FIFO)', value: 'FIFO'}],
      rule: 'FIFO',
      investment_name: '',
      investment_requirement: 0.00,
      fundcommitments: [],
      fundcommitmentheaders: [
        {text: 'Commitment ID', align: 'start', value: 'id'},
        {text: 'Fund ID', value: 'fund.id'},
        {text: 'Date', value: 'date'},
        {text: 'Fund', value: 'fund.name'},
        {text: 'Committed Amounts', value: 'amount'},
        {text: 'Undrawn Capital Commitment before Current Drawdown Notice', value: 'drawn_amount'},
        {text: 'Total Drawdown Notice', value: 'drawdown_notice'},
        {text: 'Undrawn Capital Commitment after Current Drawdown Notice', value: 'drawn_new'},
      ],
      funds: [],
      fundsheaders: [
        {text: '', align: 'start', value: 'name'},
        {text: 'Drawdown Notice', value: 'drawdown_notice'},
      ]
    }
  },
  methods: {
    async confirm() {
      const calldata = {
        date: this.date,
        investment_name: this.investment_name,
        capital_requirement: this.investment_requirement
      }

      let call_id = null
      // Insert fund call
      try {
        const resp = await this.axios({
          url: 'http://127.0.0.1:8000/api/fundcalls/',
          method: 'POST',
          data: calldata
        })
        call_id = resp.data.id
      } catch(error) {
        console.log(error)
      }

      // Insert fund investments
      if (call_id !== null) {
        this.fundcommitments.forEach(async (fund, i) => {
          if (fund['drawdown_notice'] > 0) {
            try {
              await this.axios({
                url: 'http://127.0.0.1:8000/api/fundinvestments/',
                method: 'POST',
                data: {
                  commitment_id: i+1,
                  investment_amount: fund['drawdown_notice'],
                  call: call_id,
                  fund: fund['fund']['id']
                }
              })
              await this.axios({
                url: `http://127.0.0.1:8000/api/fundcommitments/${fund['fund']['id']}/`,
                method: 'PATCH',
                data: {
                  drawn_amount: fund['drawn_new']
                }
              })
            } catch (error) {
              console.log(error)
            }
          }
        })
      }
    },
    fifo() {
      let remaining_investment_req = Number(this.investment_requirement)
      this.fundcommitments.forEach(fund => {
        let fund_remaining = fund['drawn_amount'] - remaining_investment_req
        if (fund_remaining < 0) {
          remaining_investment_req = fund_remaining * -1
          fund['drawdown_notice'] = fund['drawn_amount']
          fund['drawn_new'] = 0
        } else {
          fund['drawdown_notice'] = remaining_investment_req
          fund['drawn_new'] = fund_remaining
          remaining_investment_req = 0
        }
      })

      if (remaining_investment_req > 0) {
        alert('Not enough funds!')
        this.confirm_disabled = true
      } else {
        this.confirm_disabled = false
      }
    },
    calculate() {
      switch (this.rule) {
        case 'FIFO':
          this.fifo()
          break;
        default:
          this.fifo()
      }

      let fundsumm = {}
      this.fundcommitments.forEach(fc => {
        if (fc['fund']['id'] in fundsumm) {
          fundsumm[fc['fund']['id']] += Number(fc['drawdown_notice'])
        } else {
          fundsumm[fc['fund']['id']] = Number(fc['drawdown_notice'])
        }
      })
      this.funds.forEach(f => {
        f['drawdown_notice'] = fundsumm[f['id']]
      })
    },
    async getCommitments() {
      try {
        const commitments = await this.axios({
          url: 'http://127.0.0.1:8000/api/fundcommitments/',
          method: 'GET',
        })
        commitments.data.forEach(commitment => {
          commitment['drawdown_notice'] = 0.00
          commitment['drawn_new'] = commitment['drawn_amount']
          this.fundcommitments.push(commitment)
        })
      } catch(error) {
        console.log(error)
      }
    },
    async getFunds() {
      try {
        const funds = await this.axios({
          url: 'http://127.0.0.1:8000/api/funds/',
          method: 'GET',
        })

        funds.data.forEach(fund => {
          fund['drawdown_notice'] = 0.00
          this.funds.push(fund)
        })
      } catch(error) {
        console.log(error)
      }
    }
  },
  mounted() {
    this.getCommitments()
    this.getFunds()
  }
}
</script>
