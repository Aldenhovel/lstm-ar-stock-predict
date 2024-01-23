<template>
  <v-app>
    <v-row style="overflow: hidden; height: 80px; margin-bottom: 5px">
      <top-nav-bar></top-nav-bar>
    </v-row>
    <v-main>
      <router-view/>
    </v-main>

    <v-row>
      <bottom-nav-bar></bottom-nav-bar>
    </v-row>
  </v-app>
</template>

<script>

import BottomNavBar from "@/components/BottomNavBar";
import TopNavBar from "@/components/TopNavBar";
export default {
  name: 'App',
  components: {TopNavBar, BottomNavBar},
  data: () => ({
    //
  }),
};
</script>
