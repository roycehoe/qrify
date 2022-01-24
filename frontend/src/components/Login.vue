<script lang="ts" setup>
import { ref } from "vue";
import router from "@/router";
import { ErrorCode, ErrorMsg } from "@/services/errors";
import { AuthUserRequest, AuthUserResponse, getAuthUserResponse } from "@/services/user/getAuthUserResponse";

const loginForm = ref({} as AuthUserRequest);
const errorDisplay = ref("");
const isLoading = ref(false)

async function login(): Promise<void> {
  errorDisplay.value = ""
  isLoading.value = true
  const { ok: isSuccessful, val: response } = await getAuthUserResponse(
    loginForm.value
  );

  if (isSuccessful) {
    const { access_token: token } = response as AuthUserResponse;
    localStorage.removeItem("token");
    localStorage.setItem("token", token);
    router.push({
      path: '/dashboard',
    })
    return;
  }
  switch (response) {
    case ErrorCode.INVALID_CREDENTIALS:
      errorDisplay.value = ErrorMsg.INVALID_CREDENTIALS;
      break;
    default:
      errorDisplay.value = ErrorMsg.SOMETHING_WENT_WRONG;
  }
  isLoading.value = false
}
</script>

<template>
  <div class="login-display w-full">
    <form class="login-form" @submit.prevent="login">
      <div class="login-form__username mb-4">
        <input
          class="login-form__username--grey-input appearance-none rounded-sm relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
          type="text"
          v-model="loginForm.username"
          placeholder="Username"
          autocomplete="off"
          maxlength="20"
          required="true"
        />
      </div>

      <div class="login-form__password">
        <input
          class="login-form__password login-form__password--input appearance-none rounded-sm relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
          type="password"
          v-model="loginForm.password"
          placeholder="Password"
          autocomplete="off"
          maxlength="20"
          required="true"
        />
      </div>
      <div class="login-form__credentials-error h-8">
        <p class="text-red-500 italic">{{ errorDisplay }}</p>
      </div>

      <div
        class="login-form__login-button inline-flex items-center justify-center py-1 border border-transparent text-base rounded-sm text-white hover:bg-opacity-100 bg-opacity-90 bg-green-500 w-full cursor-pointer border-gray-300"
      >
        <button v-if="!isLoading" class="login-form__login-button--green font-semibold">Log in</button>
        <button
          v-else
          class="login-form__login-button--loading font-semibold"
          loading
          disabled
        >Loading...</button>
      </div>
    </form>

    <div class="create-account text-center">
      <div class="create-account__question m-3">
        <p class="create-account__question--txt">Don't have an account yet?</p>
      </div>

      <div
        class="create-account__link inline-flex items-center justify-center py-1 border border-gray-300 text-base font-medium rounded-sm text-black hover:bg-neutral-100 bg-neutral-50 w-full cursor-pointer"
      >
        <router-link class="create-account__link--txt" to="/new">
          <button class="create-account__link--btn font-semibold">Create an account</button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
</style>