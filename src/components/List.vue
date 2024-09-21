<script setup>
import {LISTS} from "../lists.js";

defineProps({
  index: Number,
})

</script>

<template>
  <div>
    <p class="list-item" v-for="item in LISTS[index]">
      {{item}}
    </p>
  </div>
</template>

<style scoped>
.list-item {
  font-size: 130%;
}
p {
  margin-block-end: 0;
  margin-block-start: 0;
}
</style>
