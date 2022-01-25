import { getAllQRResponse, QRResponse } from "@/services/qr/getAllQRResponse";
import { CreateQRRequest, CreateQRResponse, getCreateQRResponse } from "@/services/qr/getCreateQRResponse";
import { DeleteQRRequest, getDeleteQRResponse } from "@/services/qr/getDeleteQRResponse";
import { ref } from "vue";

export function useQRs() {

    let currentQR = ref({} as QRResponse)
    let test = ref(async () => await getAllQRs())

    async function getAllQRs() {
        const { ok: isSuccessful, val: response } = await getAllQRResponse()
        if (isSuccessful) {
            return response
        }
        console.log(response)
    }

    async function deleteQR(deleteQRForm: DeleteQRRequest) {
        const { ok: isSuccessful, val: response } = await getDeleteQRResponse(deleteQRForm)
        if (isSuccessful) {
            location.reload()
            return
        }
        console.log(response)
    }

    async function createQR(createQRForm: CreateQRRequest) {
        const { ok: isSuccessful, val: response } = await getCreateQRResponse(createQRForm)
        if (isSuccessful) {
            location.reload()
            return response as CreateQRResponse
        }
        console.log(response)
    }

    function setCurrentQR(QRData: QRResponse) {
        currentQR.value = QRData
    }

    function getCurrentQR() {
        return currentQR
    }

    return { currentQR, getAllQRs, deleteQR, createQR, setCurrentQR, getCurrentQR, test }
}