<script lang="ts" setup>
import { getAssetUrl } from '@/services/assets';


</script>

<template>
  <div class="display w-3/4 md:1/2 xl:w-2/12 mt-16 md:mt-32 p-2 m-auto">
    <div class="display__img--container flex justify-center">
      <img
        class="display__img--img h-auto w-auto md:max-h-64 xl:max-h-full"
        :src="getAssetUrl('graphics', 'logo.png')"
      />
    </div>
    <div class="display--inputBox mt-8">
      <router-view></router-view>
    </div>
  </div>
</template>

<style scoped lang="scss">
</style>