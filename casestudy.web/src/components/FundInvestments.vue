<template>
  <div>
    <v-data-table>
      <template v-slot:top>
      </template>
    </v-data-table>
  </div>
</template>

<script>
export default {
  name: 'FundInvestments',
  methods: {
    async getData() {
      //
    }
  },
  mounted() {
    this.getData()
  }
}
</script>