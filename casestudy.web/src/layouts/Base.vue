<template>
  <v-app>
    <NavBar />
    <v-content class="px-auto">
      <v-container fluid>
        <v-row align="center" justify="center">
          <v-col cols="8">
            <slot name="content-center"></slot>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
    <v-footer app>
      <slot name="footer"></slot>
    </v-footer>
  </v-app>
</template>

<script>
import NavBar from '@/components/CapitalCallNavBar.vue'

export default {
  name: 'Base',
  components: {
    NavBar
  }
}
</script>
