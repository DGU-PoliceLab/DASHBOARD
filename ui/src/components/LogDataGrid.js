import { useState } from "react";
import { DataGrid } from "@mui/x-data-grid";
import {
    systemLogColumns,
    containerLogColumns,
    moduleLogColumns,
    edgecamLogColumns,
} from "../data/logData";
import { Backdrop, Box } from "@mui/material";

export default function LogDataGrid({ open, close, target, data }) {
    let columns = [];
    if (target === "system") {
        columns = systemLogColumns;
    } else if (target === "container") {
        columns = containerLogColumns;
    } else if (target === "module") {
        columns = moduleLogColumns;
    } else if (target === "edgecam") {
        columns = edgecamLogColumns;
    }
    return (
        <Backdrop
            open={open}
            onClick={() => {
                close();
            }}
        >
            <Box
                sx={{
                    width: "calc(100svw - 4rem)",
                    maxHeight: "calc(100svh - 10rem)",
                    overflow: "auto",
                }}
                onClick={(e) => {
                    e.stopPropagation();
                    e.preventDefault();
                }}
            >
                <DataGrid
                    autoHeight
                    // checkboxSelection
                    rows={data}
                    columns={columns}
                    getRowClassName={(params) =>
                        params.indexRelativeToCurrentPage % 2 === 0
                            ? "even"
                            : "odd"
                    }
                    initialState={{
                        pagination: { paginationModel: { pageSize: 20 } },
                    }}
                    pageSizeOptions={[10, 20, 50]}
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
            </Box>
        </Backdrop>
    );
}
