<script lang="ts" setup>
import QRList from '@/components/QRList.vue';
import { onBeforeMount, onMounted, PropType, ref } from 'vue';
import TimerCreate from '@/components/TimerCreate.vue';
import Countdown from '@/components/Countdown.vue';
import { useQRs } from '@/composables/useQRs';
import { getAllQRResponse, QRResponse } from '@/services/qr/getAllQRResponse';
import { CreateQRResponse } from '@/services/qr/getCreateQRResponse';

const { getAllQRs } = useQRs()
const allQRData = ref({})

async function setDashboardInfo() {
  allQRData.value = await getAllQRs()
}

onBeforeMount(async () => await setDashboardInfo());


</script>

<template>
  <p>all qrs: {{ allQRData }}</p>
  <div class="min-h-full">
    <div class="bg-white shadow">
      <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
        <button @click="$router.push('/')" class="text-3xl font-bold text-gray-900">QR-ify</button>
      </div>
    </div>
    <div>
      <div class="max-w-7xl py-6 px-8 mx-auto">
        <div class="border-4 border-dashed border-gray-200 rounded-lg min-h-16 h-max my-10">
          <Countdown :data="timerData"></Countdown>
        </div>
        <TimerCreate></TimerCreate>
        <div class="border-4 border-dashed border-gray-200 rounded-lg min-h-16 h-max mt-10">
          <QRList :data="allQRData"></QRList>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
</style>