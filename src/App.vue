<template>
  <div>
    <div @click="onClick()">
      <List :index="index"/>
    </div>

    <iframe allow="camera; microphone" src="https://spec.sumianvoice.com/" width="1200px" height="500px"></iframe>
  </div>
</template>

<style scoped></style>

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
