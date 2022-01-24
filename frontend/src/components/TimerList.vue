<script lang="ts" setup>import { getMetricTime, TimerDisplay } from '@/services/timer/convertTime';
import { CreateTimerResponse } from '@/services/timer/getCreateTimerResponse';
import { getDashboardInfoResponse } from '@/services/timer/getDashboardDisplayResponse';
import { getDeleteTimerResponse } from '@/services/timer/getDeleteTimerResponse';
import { emit } from 'process';
import { onBeforeMount, ref } from 'vue';


const dashboardInfo = ref([] as Array<TimerDisplay>)
const countdownDisplay = ref({} as TimerDisplay)

function createDashboardDisplay(createTimerResponse: Array<CreateTimerResponse>) {
  createTimerResponse.forEach(element => {
    dashboardInfo.value.push({
      id: element.id,
      title: element.title,
      createdAt: element.created_at,
      hours: getMetricTime(element.time).hours,
      minutes: getMetricTime(element.time).minutes,
      seconds: getMetricTime(element.time).seconds,
      time: element.time
    })
  })
}



async function showDashboardInfo() {
  const { ok: isSuccessful, val: response } = await getDashboardInfoResponse()
  if (isSuccessful) {
    const createTimerResponse = response as Array<CreateTimerResponse>
    createDashboardDisplay(createTimerResponse)
    return
  }
  console.error(response)
}

async function deleteTimer(timerId: number) {
  const { ok: isSuccessful, val: response } = await getDeleteTimerResponse({ timer_id: timerId })
  if (isSuccessful) {
    location.reload()
    return
  }
  console.error(response)
}

onBeforeMount(async () => await showDashboardInfo());

</script>


<template>
  <div v-for="info in dashboardInfo">
    <div
      class="dashboardInfo__group survey bg-neutral-100 rounded-md m-2 bg-gray-50 flex justify-between"
    >
      <div class="dashboardInfo__group--txt">
        <p class="m-3 font-bold inline-block">{{ info.title }}</p>
        <kbd class="kbd font-mono m-3">
          <p>{{ info.hours }}h:</p>
          <p>{{ info.minutes }}m:</p>
          <p>{{ info.seconds }}s</p>
        </kbd>
      </div>

      <div class="dashboardInfo__group--buttons flex items-center">
        <button
          @click="$emit('emitTimerData', info)"
          class="btn btn-success bg-green-500 m-1 w-16 h-8 rounded-md hover:bg-green-600 border-none min-h-0"
        >View</button>

        <button
          class="btn btn-success bg-red-500 m-1 w-16 h-8 rounded-md hover:bg-red-600 border-none min-h-0"
          @click="deleteTimer(info.id)"
        >Delete</button>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
</style>