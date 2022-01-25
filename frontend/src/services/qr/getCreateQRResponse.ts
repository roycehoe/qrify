import { Ok, Err, Result } from "ts-results"
import { client } from "@/services"
import { ErrorCode, getErrorCode } from "@/services/errors";



export interface CreateQRRequest {
    title: string
    link: string
}

export interface CreateQRResponse {
    id: number
    created_at: any
    title: string
    link: string
    image: string
}

export async function getCreateQRResponse(createQRRequest: CreateQRRequest): Promise<Result<CreateQRResponse, ErrorCode>> {
    try {
        const response = await client.post("/QR", createQRRequest);
        return Ok(response.data as CreateQRResponse)
    }
    catch (error) {
        return Err(getErrorCode(error))
    }
}