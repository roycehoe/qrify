<script lang="ts" setup>;
import { useQRs } from '@/composables/useQRs';
import { QRResponse } from '@/services/qr/getAllQRResponse';
import { onBeforeMount, PropType, ref } from 'vue';

const { deleteQR, setCurrentQR, allQRs, getAllQRs, currentQR, getCurrentQR } = useQRs()
onBeforeMount(async () => await getAllQRs());

function test() {
  console.log(currentQR.value)
  setCurrentQR(1)
  console.log(currentQR.value)
  const test = getCurrentQR()
  console.log(test.value)
}

</script>


<template>
  <button @click="test">test here</button>
  <div v-for="QR in allQRs">
    <div
      class="dashboardInfo__group survey bg-neutral-100 rounded-md m-2 bg-gray-50 flex justify-between"
    >
      <div class="dashboardInfo__group--txt">
        <p class="m-3 font-bold inline-block">{{ QR.title }}</p>
      </div>

      <div class="dashboardInfo__group--buttons flex items-center">
        <button
          @click="setCurrentQR(QR)"
          class="btn btn-success bg-green-500 m-1 w-16 h-8 rounded-md hover:bg-green-600 border-none min-h-0"
        >View</button>

        <button
          class="btn btn-success bg-red-500 m-1 w-16 h-8 rounded-md hover:bg-red-600 border-none min-h-0"
          @click="deleteQR({ QR_id: QR.id })"
        >Delete</button>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
</style>