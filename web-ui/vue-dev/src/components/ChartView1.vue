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
        <v-btn variant="tonal" width="100%" @click="predict()" color="success">Predict</v-btn>

        <template>
          <v-card
              class="mx-auto ma-1 mt-2"
          >
            <v-list disabled>
              <v-list-item>
                <v-icon class="mr-1">mdi-chip</v-icon>
                <v-list-item-title>{{ config_device }}</v-list-item-title>
              </v-list-item>
              <hr/>
              <v-list-item>
                <v-icon class="mr-1">mdi-package</v-icon>
                <v-list-item-title>{{ config_model }}</v-list-item-title>
              </v-list-item>
              <hr/>
              <v-list-item>
                <v-icon class="mr-1">mdi-package-variant</v-icon>
                <v-list-item-title>{{ config_checkpoint }}</v-list-item-title>
              </v-list-item>
              <hr/>
              <v-list-item>
                <v-icon class="mr-1" v-if="check_conn === '0'" color="success">mdi-lan-connect</v-icon>
                <v-icon v-else class="mr-1" color="error">mdi-lan-disconnect</v-icon>
                <v-list-item-title v-if="check_conn === '0'">backend connected</v-list-item-title>
                <v-list-item-title v-else>backend offline</v-list-item-title>
              </v-list-item>
              <hr/>
              <v-list-item>
                <v-icon class="mr-1">mdi-timer</v-icon>
                <v-list-item-title>{{ conn_time }}</v-list-item-title>
              </v-list-item>

            </v-list>
          </v-card>
        </template>

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

    config_model: '--',
    config_checkpoint: '--',
    config_device: '--',

    check_conn: '-1',
    conn_time: '--',
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

    setInterval(() => {
      axios.get('/check_conn').then(response => {
        let data = response.data;
        this.check_conn = data.status;
        this.conn_time = data.conn_time;
        let config = data.config;
        this.config_model = config.model;
        this.config_checkpoint = config.checkpoint;
        this.config_device = config.device;
      }).catch(error => {
        console.log(error);
        this.check_conn = '-1';
        this.conn_time = '--';
        this.config_model = '--';
        this.config_checkpoint = '--';
        this.config_device = '--';
      })
    }, 1000)

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