<template>
  <div style="min-width: 100%">
    <div @click="onClick()" style="padding-top: 10px; padding-bottom: 10px">
      <List :index="index"/>
    </div>

    <iframe allow="camera; microphone" src="https://spec.sumianvoice.com/" width="100%" height="500px"></iframe>
  </div>
</template>

<style scoped>
@media (max-width: 600px) {
  iframe {
    height: 300px;
  }
}
</style>

<script setup>
import List from './components/List.vue'
import {LISTS} from "./lists.js";
import {ref} from "vue";

const index = ref(0);

function onClick() {
  index.value = Math.floor(Math.random()*LISTS.length);
  console.log(index)
}
</script>
