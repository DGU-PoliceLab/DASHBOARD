import { useState } from "react";
import { DataGrid } from "@mui/x-data-grid";
import { columns } from "../data/moduleData";

export default function ModuleDataGrid({ data }) {
    const [rows, setRows] = useState([
        {
            id: 1,
            name: "falldown",
            desc: "낙상을 감지하는 모듈",
            status: data["falldown"] ? "Online" : "Offline",
        },
        {
            id: 2,
            name: "longterm",
            desc: "장시간 고정 자세를 감지하는 모듈",
            status: data["longterm"] ? "Online" : "Offline",
        },
        {
            id: 3,
            name: "selfharm",
            desc: "자살 및 자해 행동을 감지하는 모듈",
            status: data["selfharm"] ? "Online" : "Offline",
        },
        {
            id: 4,
            name: "emotion",
            desc: "감정을 분석하는 모듈",
            status: data["emotion"] ? "Online" : "Offline",
        },
        {
            id: 5,
            name: "violence",
            desc: "폭행을 감지하는 모듈",
            status: data["violence"] ? "Online" : "Offline",
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
