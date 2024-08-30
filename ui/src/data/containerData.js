import * as React from "react";
import Avatar from "@mui/material/Avatar";
import Chip from "@mui/material/Chip";

function renderStatus(status) {
    const colors = {
        Online: "success",
        Offline: "error",
    };

    return <Chip label={status} color={colors[status]} size="small" />;
}

export function renderAvatar(params) {
    if (params.value == null) {
        return "";
    }

    return (
        <Avatar
            sx={{
                backgroundColor: params.value.color,
                width: "24px",
                height: "24px",
                fontSize: "0.85rem",
            }}
        >
            {params.value.name.toUpperCase().substring(0, 1)}
        </Avatar>
    );
}

export const columns = [
    { field: "name", headerName: "컨테이너명", flex: 1, minWidth: 100 },
    {
        field: "desc",
        headerName: "설명",
        flex: 2,
        minWidth: 200,
    },
    {
        field: "status",
        headerName: "상태",
        flex: 0.5,
        minWidth: 80,
        renderCell: (params) => renderStatus(params.value),
    },
];
