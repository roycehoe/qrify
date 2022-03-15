const envFile = import.meta.env as EnvVariables

interface EnvVariables {
    VITE_BASE_URL?: string
}

function getBaseURL(envValue: string | undefined, defaultValue: string): string {
    if (envValue) {
        return envValue
    }
    return defaultValue
}

export const baseURL = getBaseURL(envFile.VITE_BASE_URL, "https://qrify.fancybinary.sg/api")
