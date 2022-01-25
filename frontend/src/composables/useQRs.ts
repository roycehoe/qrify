import { ErrorCode } from "@/services/errors";
import { getAllQRResponse, QRResponse } from "@/services/qr/getAllQRResponse";
import { CreateQRRequest, CreateQRResponse, getCreateQRResponse } from "@/services/qr/getCreateQRResponse";
import { DeleteQRRequest, getDeleteQRResponse } from "@/services/qr/getDeleteQRResponse";
import { ref } from "vue";

export const currentQR = ref({} as QRResponse)

export function useQRs() {

    const allQRs = ref({} as Array<QRResponse>)

    async function getAllQRs(): Promise<void> {
        const { ok: isSuccessful, val: response } = await getAllQRResponse()
        if (isSuccessful) {
            allQRs.value = response as Array<QRResponse>
            return
        }
        console.log(response as ErrorCode)
    }

    async function deleteQR(deleteQRForm: DeleteQRRequest) {
        const { ok: isSuccessful, val: response } = await getDeleteQRResponse(deleteQRForm)
        if (isSuccessful) {
            location.reload()
            return
        }
        console.log(response as ErrorCode)
    }

    async function createQR(createQRForm: CreateQRRequest) {
        const { ok: isSuccessful, val: response } = await getCreateQRResponse(createQRForm)
        if (isSuccessful) {
            location.reload()
            return response as CreateQRResponse
        }
        console.log(response as ErrorCode)
    }

    function setCurrentQR(QRData: QRResponse) {
        currentQR.value = QRData as QRResponse
    }

    function getCurrentQR() {
        return currentQR
    }

    return { currentQR, allQRs, getAllQRs, deleteQR, createQR, setCurrentQR, getCurrentQR }
}