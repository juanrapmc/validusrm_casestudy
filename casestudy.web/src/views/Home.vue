<template>
  <CapitalCallBase>
    <template v-slot:content-center>
    </template>
  </CapitalCallBase>
</template>

<script>
// @ is an alias to /src
import CapitalCallBase from '@/layouts/Base.vue'

export default {
  name: 'Home',
  components: {
    CapitalCallBase,
  }
}
</script>
