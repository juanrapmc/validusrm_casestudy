<template>
  <div>
    <v-data-table
      :items="tabledata"
      :headers="tableheaders"
      hide-default-footer
    >
      <template v-slot:top>
      </template>
    </v-data-table>
  </div>
</template>

<script>
export default {
  name: 'FundInvestments',
  data() {
    return {
      tabledata: [],
      tableheaders: [
        {
          text: 'Date',
          align: 'start',
          value: 'date'
        },
        { text: 'Call #', value: 'call' },
      ]
    }
  },
  methods: {
    async getData() {
      try {
        const fundcalls = await this.axios({
          url: 'http://127.0.0.1:8000/api/fundcalls/',
          method: 'GET'
        })
        const fundinvestments = await this.axios({
          url: 'http://127.0.0.1:8000/api/fundinvestments',
          method: 'GET'
        })

        let d = {}
        fundcalls.data.forEach(call => {
          d[call.id] = { date: call.date, call: call.id }
        })
        fundinvestments.data.forEach(inv => {
          d[inv.call]['fund_'+inv.fund] = inv.investment_amount
        })
        Object.keys(d).forEach(k => {
          this.tabledata.push(d[k])
        })
      } catch(error) {
        console.log(error)
      }
    },
    async getFunds() {
      try {
        const funds = await this.axios({
          url: 'http://127.0.0.1:8000/api/funds/',
          method: 'GET'
        })
        funds.data.forEach(f => {
          this.tableheaders.push({ 'text': f.name, 'value': 'fund_'+f.id })
        });
      } catch(error) {
        console.log(error)
      }
    }
  },
  mounted() {
    this.getFunds()
    this.getData()
  }
}
</script>