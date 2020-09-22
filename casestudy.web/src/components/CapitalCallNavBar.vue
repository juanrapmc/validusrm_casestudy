<template>
  <v-app-bar absolute app dense>
    <v-toolbar-title class="px-12">
      <v-btn to="/" text>
        <v-img
          :src="require('../assets/validus.png')"
          class="my-3"
          contain
          height="200"
        /></v-btn>
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items class="px-12">
      <v-btn to="/capitalcall/dashboard" text>Dashboard</v-btn>
      <v-btn to="/capitalcall/new" text>New Call</v-btn>
    </v-toolbar-items>
  </v-app-bar>
</template>

<script>
export default {
  name: 'NavBar',
  methods: {
  },
  computed: {
  }
}
</script>
