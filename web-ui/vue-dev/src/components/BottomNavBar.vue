<template>
<div class="bottomNavBar">
  <v-app>
        <v-bottom-navigation
          :value="value"
          color="primary"
          width="100%"
          style="position: fixed"
        >


          <v-btn
            v-for="item in labels" v-bind:key="item.id"
            height="100%"
            style="background-color: white"
            @click="goto(item.to)"
          >
              <span>{{ item.name }}</span>
              <v-icon>{{ item.icon }}</v-icon>
          </v-btn>



        </v-bottom-navigation>

  </v-app>
</div>
</template>

<script>
export default {
  name: "BottomNavBar",
  data() {
    return {
      labels: [
        { name: "Dashboard", icon: "mdi-chart-areaspline", to: "/chart1"},
        { name: "information", icon: "mdi-information", to: "/chart2"},

      ]
    }
  },
  methods: {
    goto(to) {
      this.$router.replace(to)

    }
  }
}
</script>

<style scoped>
</style>