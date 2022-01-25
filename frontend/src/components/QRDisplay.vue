<script lang="ts" setup>import { currentQR, useQRs } from '@/composables/useQRs';
import { onBeforeMount, ref } from 'vue';

function getQRURI(base64Data: string) {
  return `data:image/png;base64,${base64Data}`
}



</script>



<template>
  <div class="flex flex-col justify-center items-center">
    <p class="stat-title text-3xl mt-8">{{ currentQR.title }}</p>
    <img v-if="currentQR.image" class="w-80" :src="getQRURI(currentQR.image)" />
  </div>
</template>