<template>
  <v-container>
    <v-row>
      <v-col cols="9">
        Beam Search
        <v-card class="mx-auto ma-1" outlined elevation="3" width="100%">
          <v-img :src="gs_img"/>
        </v-card>
        Greedy Search
        <v-card class="mx-auto ma-1" outlined elevation="3" width="100%">
          <v-img :src="bs_img"/>
        </v-card>
      </v-col>

      <v-col cols="3">
        <v-text-field clearable label="Stock Code" variant="solo-filled" v-model="code" v-on:focus="codeFocus" v-on:blur="codeBlur" placeholder="300001"></v-text-field>
        Select a date to predict:
        <v-date-picker width="100%" v-model="endDate"></v-date-picker>
        <v-btn variant="tonal" width="100%" @click="predict()">Predict</v-btn>

      </v-col>
    </v-row>
  </v-container>


</template>

<script>
//import * as echarts from 'echarts'
//import eventbus from "@/eventbus";
import axios from "axios"

export default {
name: "ChartView1",
  data: () => ({
    endDate: '2024-01-22',
    code: '300001.SZ',
    bs_img: 'https://cdn.vuetifyjs.com/images/parallax/material.jpg',
    gs_img: 'https://cdn.vuetifyjs.com/images/parallax/material.jpg',
    blur: false,
  }),
  methods: {
    codeFocus() {
      var codeHead = this.code.substr(0, 2);
      if (codeHead === '30' || codeHead === '60' || codeHead === '00' || codeHead === '68') {
        this.code = this.code.substr(0, this.code.length - 3)
      }
    },
    codeBlur() {
      var codeHead = this.code.substr(0, 2);
      if (codeHead === '30' || codeHead === '00') {
        this.code = this.code + '.SZ';
      }
      else if (codeHead === '60' || codeHead === '68') {
        this.code = this.code + '.SH';
      }
      else {
        //alert('code should be started with 00/30/60/68 .');
        this.code = ''
      }
    },
    predict() {
      this.bs_img = '';
      this.gs_img = '';
      axios.post('/predict', {
        code: this.code,
        endDate: this.endDate,
      }).then(response => {
        let data = response.data;
        this.bs_img = data.bs_img;
        this.gs_img = data.gs_img;
      })
    }
  },
  mounted() {

  },
  watch: {
    endDate(ov, nv) {
      console.log(ov, nv);
    },
    code(nv, ov) {
      console.log(nv, ov);
    }

  }
}
</script>

<style scoped>

</style>