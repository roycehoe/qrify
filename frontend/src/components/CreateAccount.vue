<script lang="ts" setup>
import { ref } from "vue";
import { ErrorCode, ErrorMsg } from "@/services/errors";
import { CreateUserRequest, getCreateUserResponse } from "@/services/user/getCreateUserResponse";

const newUserForm = ref({} as CreateUserForm);
const errorDisplay = ref("");
const isLoading = ref(false)
const accountCreated = ref(false);

interface CreateUserForm extends CreateUserRequest {
  confirmPassword: string;
}

async function createAccount(): Promise<void> {
  isLoading.value = true
  if (newUserForm.value.password != newUserForm.value.confirmPassword) {
    errorDisplay.value = ErrorMsg.NON_MATCHING_PASSWORDS;
    isLoading.value = false
    return
  }
  const { ok: isSuccessful, val: response } = await getCreateUserResponse(
    newUserForm.value
  );
  if (isSuccessful) {
    accountCreated.value = true;
    isLoading.value = false
    return;
  }
  switch (response) {
    case ErrorCode.USERNAME_TAKEN:
      errorDisplay.value = ErrorMsg.USERNAME_TAKEN;
      break;
    default:
      errorDisplay.value = ErrorMsg.SOMETHING_WENT_WRONG;
  }
  isLoading.value = false
}

</script>

<template>
  <form class="create-account-form" v-if="!accountCreated" @submit.prevent="createAccount">
    <div class="create-account-form__input">
      <div class="my-2">
        <input
          class="appearance-none rounded-sm relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
          type="text"
          v-model="newUserForm.username"
          placeholder="New Username"
          autocomplete="off"
          required="true"
          maxlength="20"
          minlength="8"
        />
      </div>

      <div class="my-2">
        <input
          class="appearance-none rounded-sm relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
          type="password"
          v-model="newUserForm.password"
          placeholder="Password"
          autocomplete="off"
          required="true"
          maxlength="20"
          minlength="8"
        />
      </div>

      <div class="my-2">
        <input
          class="appearance-none rounded-sm relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
          type="password"
          v-model="newUserForm.confirmPassword"
          placeholder="Confirm Password"
          autocomplete="off"
          required="true"
          maxlength="20"
          minlength="8"
        />
      </div>
    </div>

    <div class="mb-5">
      <p class="text-red-500 italic">{{ errorDisplay }}</p>
    </div>

    <div
      class="login-form__login-button inline-flex items-center justify-center py-1 border border-transparent text-base rounded-sm text-white hover:bg-opacity-100 bg-opacity-90 bg-green-500 w-full cursor-pointer border-gray-300"
    >
      <button v-if="!isLoading" class="font-semibold">
        <p class="create-account-form__btn__txt">Create Account</p>
      </button>

      <button v-else class="font-semibold" type="submit">
        <p class="create-account-form__btn__txt">Loading...</p>
      </button>
    </div>

    <button
      @click="$router.push('/')"
      class="create-account__link inline-flex items-center justify-center py-1 border border-gray-300 text-base font-medium rounded-sm text-black hover:bg-neutral-100 bg-neutral-50 w-full cursor-pointer my-4"
    >
      <p class="create-account-form__btn__txt">Return to Main Menu</p>
    </button>
  </form>

  <div class="createAccountSuccess" v-else>
    <p class="text-center font-semibold">Account successfully created</p>
    <button
      class="create-account__link inline-flex items-center justify-center py-1 border border-gray-300 text-base font-medium rounded-sm text-black hover:bg-neutral-100 bg-neutral-50 w-full cursor-pointer my-4"
      @click="$router.push('/')"
      type="button"
    >
      <p class="createAccountForm__btn__txt">Return to Main Menu</p>
    </button>
  </div>
</template>

<style scoped lang="scss">
.create-account-form {
  &__input {
    &--margin {
      margin-top: 1vh;
      margin-bottom: 1vh;
    }
  }
  &__btn {
    &--green {
      margin-top: 1vh;
      width: 100%;
    }
    &--grey {
      margin-top: 1vh;
      width: 100%;
    }
  }
}
</style>