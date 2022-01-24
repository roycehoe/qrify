import { Ok, Err, Result } from "ts-results"
import { client } from "@/services"
import { ErrorCode, getErrorCode } from "@/services/errors";
import { CreateQRResponse } from "./getCreateQRResponse";

export interface AllQRResponse extends CreateQRResponse {
}

export async function getDashboardInfoResponse(): Promise<Result<Array<AllQRResponse>, ErrorCode>> {
    try {
        const response = await client.get("/QR");
        return Ok(response.data as Array<AllQRResponse>)
    }
    catch (error) {
        return Err(getErrorCode(error))
    }
}