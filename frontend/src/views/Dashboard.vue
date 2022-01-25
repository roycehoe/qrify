<script lang="ts" setup>
import QRList from '@/components/QRList.vue';
import QRCreate from '@/components/QRCreate.vue';
import QRDisplay from '@/components/QRDisplay.vue';

</script>

<template>
  <div class="min-h-full">
    <div class="bg-white shadow">
      <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
        <button @click="$router.push('/')" class="text-3xl font-bold text-gray-900">QR-ify</button>
      </div>
    </div>
    <div>
      <div class="max-w-7xl py-6 px-8 mx-auto">
        <div class="border-4 border-dashed border-gray-200 rounded-lg min-h-16 h-max my-10">
          <QRDisplay></QRDisplay>
        </div>
        <QRCreate></QRCreate>
        <div class="border-4 border-dashed border-gray-200 rounded-lg min-h-16 h-max mt-10">
          <QRList></QRList>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
</style>