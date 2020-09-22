<template>
  <CapitalCallBase>
    <template v-slot:content-left>
      <FundInvestments />
    </template>
    <template v-slot:content-right>
    </template>
  </CapitalCallBase>
</template>

<script>
// @ is an alias to /src
import CapitalCallBase from '@/layouts/Base.vue'
import FundInvestments from '@/components/FundInvestments.vue'

export default {
  name: 'CapitalCallDashboard',
  components: {
    CapitalCallBase,
    FundInvestments,
  },
  methods: {
  },
  mounted() {
  }
}
</script>