import { useState } from "react";
import { DataGrid } from "@mui/x-data-grid";
import { columns } from "../data/containerData";

export default function ContainerDataGrid({ data }) {
    const [rows, setRows] = useState([
        {
            id: 1,
            name: "pls-web",
            desc: "웹 호스팅을 위한 컨테이너",
            status: data["web"] ? "Online" : "Offline",
        },
        {
            id: 2,
            name: "pls-was",
            desc: "서비스 구동을 위한 컨테이너",
            status: data["was"] ? "Online" : "Offline",
        },
        {
            id: 3,
            name: "pls-module",
            desc: "인공지능 모듈 구동을 위한 컨테이너",
            status: data["module"] ? "Online" : "Offline",
        },
        {
            id: 4,
            name: "pls-mysql",
            desc: "기반 데이터 저장을 위한 컨테이너",
            status: data["mysql"] ? "Online" : "Offline",
        },
        {
            id: 5,
            name: "pls-redis",
            desc: "임시 및 캐싱 데이터 저장을 위한 컨테이너",
            status: data["redis"] ? "Online" : "Offline",
        },
    ]);
    return (
        <DataGrid
            autoHeight
            // checkboxSelection
            rows={rows}
            columns={columns}
            getRowClassName={(params) =>
                params.indexRelativeToCurrentPage % 2 === 0 ? "even" : "odd"
            }
            initialState={{
                pagination: { paginationModel: { pageSize: 20 } },
            }}
            // pageSizeOptions={[10, 20, 50]}
            disableColumnResize
            density="compact"
            slotProps={{
                filterPanel: {
                    filterFormProps: {
                        logicOperatorInputProps: {
                            variant: "outlined",
                            size: "small",
                        },
                        columnInputProps: {
                            variant: "outlined",
                            size: "small",
                            sx: { mt: "auto" },
                        },
                        operatorInputProps: {
                            variant: "outlined",
                            size: "small",
                            sx: { mt: "auto" },
                        },
                        valueInputProps: {
                            InputComponentProps: {
                                variant: "outlined",
                                size: "small",
                            },
                        },
                    },
                },
            }}
        />
    );
}
