<script lang="ts" setup>;
import { useQRs } from '@/composables/useQRs';
import { QRResponse } from '@/services/qr/getAllQRResponse';
import { onBeforeMount, PropType, ref } from 'vue';

const { deleteQR, setCurrentQR } = useQRs()

const props = defineProps({
  data: {
    type: Object as PropType<Array<QRResponse>>
  }
})


</script>


<template>
  <div v-for="info in data">
    <div
      class="dashboardInfo__group survey bg-neutral-100 rounded-md m-2 bg-gray-50 flex justify-between"
    >
      <div class="dashboardInfo__group--txt">
        <p class="m-3 font-bold inline-block">{{ info.title }}</p>
      </div>

      <div class="dashboardInfo__group--buttons flex items-center">
        <button
          @click="setCurrentQR(info)"
          class="btn btn-success bg-green-500 m-1 w-16 h-8 rounded-md hover:bg-green-600 border-none min-h-0"
        >View</button>

        <button
          class="btn btn-success bg-red-500 m-1 w-16 h-8 rounded-md hover:bg-red-600 border-none min-h-0"
          @click="deleteQR({ QR_id: info.id })"
        >Delete</button>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
</style>