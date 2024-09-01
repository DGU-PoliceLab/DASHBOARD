import * as React from "react";
import Chip from "@mui/material/Chip";

function renderStatus(status) {
    const colors = {
        Online: "success",
        Offline: "error",
    };

    return <Chip label={status} color={colors[status]} size="small" />;
}

export const columns = [
    { field: "name", headerName: "모듈명", flex: 0.5, minWidth: 80 },
    {
        field: "desc",
        headerName: "설명",
        flex: 2,
        minWidth: 200,
    },
    {
        field: "status",
        headerName: "상태",
        headerAlign: "center",
        align: "center",
        flex: 0.5,
        minWidth: 80,
        maxWidth: 80,
        renderCell: (params) => renderStatus(params.value),
    },
];
