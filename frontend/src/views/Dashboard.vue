<script lang="ts" setup>
import TimerList from '@/components/TimerList.vue';
import { PropType, ref } from 'vue';
import TimerCreate from '@/components/TimerCreate.vue';
import Countdown from '@/components/Countdown.vue';
import { TimerDisplay } from '@/services/timer/convertTime';

const props = defineProps({
  timerData: {
    type: Object as PropType<TimerDisplay>
  }
})

const timerData = ref({} as TimerDisplay)

function updateTimerData(emittedTimerData: TimerDisplay) {
  timerData.value = emittedTimerData
}



</script>

<template>
  <div class="min-h-full">
    <div class="bg-white shadow">
      <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
        <button @click="$router.push('/')" class="text-3xl font-bold text-gray-900">Kount</button>
      </div>
    </div>
    <div>
      <div class="max-w-7xl py-6 px-8 mx-auto">
        <div class="border-4 border-dashed border-gray-200 rounded-lg min-h-16 h-max my-10">
          <Countdown :data="timerData"></Countdown>
        </div>
        <TimerCreate></TimerCreate>
        <div class="border-4 border-dashed border-gray-200 rounded-lg min-h-16 h-max mt-10">
          <TimerList @emitTimerData="updateTimerData"></TimerList>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
</style>