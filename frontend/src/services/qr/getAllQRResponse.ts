import { Ok, Err, Result } from "ts-results"
import { client } from "@/services"
import { ErrorCode, getErrorCode } from "@/services/errors";
import { CreateQRResponse } from "./getCreateQRResponse";

export interface QRResponse extends CreateQRResponse {
}

export async function getAllQRResponse(): Promise<Result<Array<QRResponse>, ErrorCode>> {
    try {
        const response = await client.get("/QR");
        return Ok(response.data as Array<QRResponse>)
    }
    catch (error) {
        return Err(getErrorCode(error))
    }
}