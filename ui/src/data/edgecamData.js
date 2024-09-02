import * as React from "react";
import Chip from "@mui/material/Chip";

function renderStatus(status) {
    const colors = {
        Online: "success",
        Offline: "error",
        None: "default",
    };

    return <Chip label={status} color={colors[status]} size="small" />;
}

export const columns = [
    { field: "name", headerName: "엣지카메라명", flex: 2, minWidth: 100 },
    {
        field: "camera",
        headerName: "실상 카메라",
        flex: 0.5,
        minWidth: 80,
        renderCell: (params) => renderStatus(params.value),
    },
    {
        field: "thermal",
        headerName: "열화상 센서",
        flex: 0.5,
        minWidth: 80,
        renderCell: (params) => renderStatus(params.value),
    },
    {
        field: "rader",
        headerName: "레이더 센서",
        flex: 0.5,
        minWidth: 80,
        renderCell: (params) => renderStatus(params.value),
    },
    {
        field: "toilet_rader",
        headerName: "화장실 레이더 센서",
        flex: 0.5,
        minWidth: 80,
        renderCell: (params) => renderStatus(params.value),
    },
];
