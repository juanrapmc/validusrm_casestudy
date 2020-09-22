<template>
  <CapitalCallBase>
    <template v-slot:content-left>
      <CallCalculator />
    </template>
  </CapitalCallBase>
</template>>
<script>
// @ is an alias to /src
import CapitalCallBase from '@/layouts/Base.vue'
import CallCalculator from '@/components/CallCalculator.vue'

export default {
  name: 'CapitalCallNew',
  components: {
    CapitalCallBase,
    CallCalculator,
  }
}
</script>