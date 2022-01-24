import { Ok, Err, Result } from "ts-results"
import { client } from "@/services"
import { ErrorCode, getErrorCode } from "@/services/errors";

export interface DeleteQRRequest {
    QR_id: number
}


export async function getDeleteTimerResponse(deleteQRForm: DeleteQRRequest): Promise<Result<void, ErrorCode>> {
    try {
        const response = await client.delete("/QR", { data: deleteQRForm });
        return Ok(response.data as void)
    }
    catch (error) {
        return Err(getErrorCode(error))
    }
}