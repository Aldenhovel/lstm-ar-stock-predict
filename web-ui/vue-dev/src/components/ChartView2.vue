<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card class="mx-auto" outlined elevation="3" height="600">


          <template>
            <div class="text-center">
              <v-btn color="primary" @click="dialog = true" class="ma-2" width="50%">
                VERSION: BETA 0.0.1
              </v-btn>
              <v-dialog v-model="dialog" width="auto">
                <v-card>
                  <v-card-text style="width: 50vw">
                    <br/>
                    Version: BETA 0.0.1
                    <br/>
                    Update: 2024-1-22
                    <br/>
                  </v-card-text>
                </v-card>
              </v-dialog>
            </div>

            <div class="text-center">
              <v-btn color="primary" @click="mit = true" class="ma-2" width="50%">
                License
              </v-btn>
              <v-dialog v-model="mit" width="auto">
                <v-card>
                  <v-card-text style="width: 50vw">
                    <br/>
                    MIT License
                    <br/>
                  </v-card-text>
                </v-card>
              </v-dialog>
            </div>

            <div class="text-center">
              <v-btn color="primary" @click="declaration = true" class="ma-2" width="50%">
                Declaration
              </v-btn>
              <v-dialog v-model="declaration" width="auto">
                <v-card>
                  <v-card-text style="width: 50vw">
                    <br/>
                    这个项目并非为了研究金融交易投资工具，实际上这是我研究 Image Caption 任务时突发奇想做的小玩具。因为没有经过经济学或者投资策略上的专业设计，效果不好很正常，你可以自己改进。
                    <br/>
                    This project is not to study financial trading investment tools. In fact, it is a small toy that I made on a whim when I was studying the Image Caption task. Because it has not been professionally designed in terms of economics or investment strategies, it is normal for the results to be poor, and you can improve it yourself.
                    <br/>
                  </v-card-text>
                </v-card>
              </v-dialog>
            </div>

            <div class="text-center">
              <v-btn color="primary" @click="thx = true" class="ma-2" width="50%">
                About
              </v-btn>
              <v-dialog v-model="thx" width="auto">
                <v-card>
                  <v-card-text style="width: 50vw">
                    <br/>
                    Author: Aldenhovel (J.B.Liang)
                    <br/>
                    Email: 1736724492@qq.com
                    <br/>
                    GitHub: https://github.com/Aldenhovel/lstm-ar-stock-predict
                    <br/>
                  </v-card-text>
                </v-card>
              </v-dialog>
            </div>

          </template>


        </v-card>
      </v-col>


    </v-row>
  </v-container>


</template>
<script>



export default {
  name: "ChartView2",
  data: () => ({
    dialog: false,
    mit: false,
    declaration: false,
    thx: false,
  }),
  mounted() {

  }
}
</script>

<style scoped>

</style>