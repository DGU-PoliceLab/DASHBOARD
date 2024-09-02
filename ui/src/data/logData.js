import * as React from "react";
import Chip from "@mui/material/Chip";

function renderStatus(status) {
    const colors = {
        info: "success",
        warn: "warning",
        error: "error",
    };

    return <Chip label={status} color={colors[status]} size="small" />;
}

export const systemLogColumns = [
    { field: "id", headerName: "No", flex: 1, minWidth: 40 },
    {
        field: "level",
        headerName: "레벨",
        flex: 1,
        minWidth: 40,
        renderCell: (params) => renderStatus(params.value),
    },
    { field: "occurred_at", headerName: "일시", flex: 2, minWidth: 80 },
    { field: "cpu_usage", headerName: "CPU(%)", flex: 1, minWidth: 40 },
    { field: "cpu_usage_core", headerName: "코어(%)", flex: 1, minWidth: 40 },
    { field: "gpu_usage_rate", headerName: "GPU(%)", flex: 1, minWidth: 40 },
    {
        field: "gpu_mem_usage_rate",
        headerName: "GPU 메모리(%)",
        flex: 1,
        minWidth: 40,
    },
    {
        field: "gpu_mem_usage",
        headerName: "GPU 메모리(MB)",
        flex: 1,
        minWidth: 40,
    },
    {
        field: "memory_usage_rate",
        headerName: "메모리(%)",
        flex: 1,
        minWidth: 40,
    },
    { field: "memory_usage", headerName: "메모리(MB)", flex: 2, minWidth: 80 },
    {
        field: "storage_usage_rate",
        headerName: "저장소(%)",
        flex: 1,
        minWidth: 40,
    },
    { field: "storage_usage", headerName: "저장소(MB)", flex: 2, minWidth: 80 },
];

export const containerLogColumns = [
    { field: "id", headerName: "No", flex: 1, minWidth: 40 },
    {
        field: "level",
        headerName: "레벨",
        flex: 1,
        minWidth: 40,
        renderCell: (params) => renderStatus(params.value),
    },
    { field: "occurred_at", headerName: "일시", flex: 2, minWidth: 80 },
    { field: "web", headerName: "pls-web", flex: 1, minWidth: 40 },
    { field: "was", headerName: "pls-was", flex: 1, minWidth: 40 },
    { field: "module", headerName: "pls-module", flex: 1, minWidth: 40 },
    {
        field: "mysql",
        headerName: "pls-mysql",
        flex: 1,
        minWidth: 40,
    },
    {
        field: "redis",
        headerName: "pls-redis",
        flex: 1,
        minWidth: 40,
    },
    {
        field: "is_error",
        headerName: "오류발생",
        flex: 1,
        minWidth: 40,
    },
];

export const edgecamLogColumns = [
    { field: "id", headerName: "No", flex: 1, minWidth: 40 },
    {
        field: "level",
        headerName: "레벨",
        flex: 1,
        minWidth: 40,
        renderCell: (params) => renderStatus(params.value),
    },
    { field: "occurred_at", headerName: "일시", flex: 2, minWidth: 80 },
    { field: "edgecam", headerName: "상세정보", flex: 5, minWidth: 200 },
    {
        field: "is_error",
        headerName: "오류발생",
        flex: 1,
        minWidth: 40,
    },
];
