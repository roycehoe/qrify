<script lang="ts" setup>
import { ref } from 'vue';
import PlusIcon from './Icons/PlusIcon.vue';
import MinusIcon from './Icons/MinusIcon.vue';
import { CreateQRRequest } from '@/services/qr/getCreateQRResponse';
import { useQRs } from '@/composables/useQRs';

const { createQR } = useQRs()

const isCreateQR = ref(false)
const createQRForm = ref({} as CreateQRRequest)


</script>

<template>
  <button
    class="create-timer-form__toggle hover:bg-neutral-100 flex flex-row"
    @click="isCreateQR = !isCreateQR"
  >
    <div class="flex">
      <MinusIcon class="mb-2" v-if="isCreateQR"></MinusIcon>
      <PlusIcon class="mb-2" v-else></PlusIcon>
      <p class="ml-2">Create a new QR code</p>
    </div>
  </button>
  <div class="divider"></div>

  <div v-if="isCreateQR" class="flex flex-col">
    <form @submit.prevent="createQR(createQRForm)">
      <div class="form-control">
        <input
          type="text"
          placeholder="QR name"
          maxlength="50"
          required
          class="input input-info input-bordered"
          v-model="createQRForm.title"
        />
      </div>
      <div class="form-control mt-6">
        <input
          type="text"
          placeholder="QR link"
          maxlength="100"
          class="input input-info input-bordered"
          required
          v-model="createQRForm.link"
        />
      </div>
      <div class="timer-form--display__group flex justify-center my-8">
        <div class="timer-form--display grid grid-flow-col gap-5 text-center auto-cols-max"></div>
        <button class="btn btn-success bg-green-500 border-none hover:bg-green-600">Create Timer</button>
      </div>
    </form>
  </div>
</template>

<style scoped lang="scss">
</style>