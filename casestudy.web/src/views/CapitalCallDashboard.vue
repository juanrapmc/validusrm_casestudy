<template>
  <CapitalCallBase>
    <template v-slot:content-left>
    </template>
    <template v-slot:content-right>
    </template>
  </CapitalCallBase>
</template>

<script>
// @ is an alias to /src
import CapitalCallBase from '@/layouts/Base.vue'

export default {
  name: 'CapitalCallDashboard',
  components: {
    CapitalCallBase
  },
  methods: {
    getDashboardData() {
      // TODO: Get fund call and fund investments
    }
  },
  mounted() {
    this.getDashboardData()
  }
}
</script>