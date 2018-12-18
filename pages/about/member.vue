<template>
  <v-layout justify-center>
    <v-flex xs5>
      <v-layout column justify-center wrap>
        <v-flex mb-5 v-for="i in 4" :key="i">
          <v-card>
            <v-card-title>
              姓名
            </v-card-title>
            <v-card-text>
              介绍
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-flex>
  </v-layout>
</template>
