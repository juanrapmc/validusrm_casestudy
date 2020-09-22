<template>
  <v-app>
    <NavBar />
    <v-content class="px-auto">
      <v-container fluid>
        <v-row>
          <v-col cols="6" sm="12" md="6">
            <slot name="content-left"></slot>
          </v-col>
          <v-col cols="6" sm="12" md="6">
            <slot name="content-right"></slot>
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
