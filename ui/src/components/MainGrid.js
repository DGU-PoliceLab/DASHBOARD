import { useState, useEffect } from "react";
import Grid from "@mui/material/Grid2";
import Box from "@mui/material/Box";
import Chip from "@mui/material/Chip";
import Typography from "@mui/material/Typography";
import Copyright from "../internals/components/Copyright";
import Button from "@mui/material/IconButton";
import FormatListBulletedIcon from "@mui/icons-material/FormatListBulleted";
// import SystemChart from "./SystemChart";
import StatCard from "./StatCard";
import ContainerDataGrid from "./ContainerDataGrid";
import ModuleDataGrid from "./ModuelDataGrid";
import EdgecamDataGrid from "./EdgecamDataGrid";
import axios from "axios";
import {
    convSystemData,
    convContainerData,
    convModuleData,
    convEdgecamData,
    convSystemLog,
    convContainerLog,
    convModuleLog,
    convEdgecamLog,
} from "../data/DataConverter";
import LogDataGrid from "./LogDataGrid";

export default function MainGrid() {
    const [systemStatus, setSystemStatus] = useState("정상");
    const [containerStatus, setConatinerStatus] = useState("정상");
    const [moduleStatus, setModuleStatus] = useState("정상");
    const [edgecamStatus, setEdgecamStatus] = useState("정상");
    const [system, setSystem] = useState([
        {
            title: "CPU",
            value: "0% 사용중",
            percent: 0,
            gap: 0,
            data: [],
        },
        {
            title: "GPU",
            value: "0% 사용중",
            percent: 0,
            gap: 0,
            data: [],
        },
        {
            title: "메모리",
            value: "0% 사용중",
            percent: 0,
            gap: 0,
            data: [],
        },
        {
            title: "저장소",
            value: "0% 사용됨",
            percent: 0,
            gap: 0,
            data: [],
        },
    ]);
    const [container, setContainer] = useState([]);
    const [module, setModule] = useState([]);
    const [edgecam, setEdgecam] = useState([]);
    const [logTarget, setLogTarget] = useState("");
    const [log, setLog] = useState([]);
    const getData = async () => {
        const response = await axios.get("http://localhost:8000/live");
        const data = response["data"];
        setSystemData(data["system"]);
        setContainerData(data["container"]);
        setModuleData(data["module"]);
        setEdgecamData(data["edgecam"]);
    };
    const getLog = async (target) => {
        setLogTarget(target);
        let convData = [];
        if (target !== "") {
            const response = await axios.get(
                "http://localhost:8000/log?target=" + target
            );
            const data = response["data"];
            console.table(data[target]);
            if (target === "system") {
                convData = convSystemLog(data[target]);
            } else if (target === "container") {
                convData = convContainerLog(data[target]);
            } else if (target === "module") {
                convData = convModuleLog(data[target]);
            } else if (target === "edgecam") {
                convData = convEdgecamLog(data[target]);
            }
        }
        setLog(convData);
    };
    const setSystemData = (systemData) => {
        setSystemStatus(systemData["status"]);
        const convData = convSystemData(systemData, system);
        setSystem(convData);
    };
    const setContainerData = (containerData) => {
        setConatinerStatus(containerData["status"]);
        const convData = convContainerData(containerData);
        setContainer(convData);
    };
    const setModuleData = (moduleData) => {
        setModuleStatus(moduleData["status"]);
        const convData = convModuleData(moduleData);
        setModule(convData);
    };
    const setEdgecamData = (edgecamData) => {
        setEdgecamStatus(edgecamData["status"]);
        const convData = convEdgecamData(edgecamData["edgecam"]);
        setEdgecam(convData);
    };
    useEffect(() => {
        getData();
        const timer = setInterval(() => {
            getData();
        }, 3000);
        return () => clearInterval(timer);
    }, []);

    return (
        <Box sx={{ width: "100%", maxWidth: { sm: "100%", md: "1700px" } }}>
            <Box
                sx={{
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "space-between",
                    mb: 2,
                }}
            >
                <Typography component="h2" variant="h6">
                    시스템{" "}
                    <Chip
                        size="medium"
                        color={systemStatus === "정상" ? "success" : "error"}
                        label={systemStatus}
                    />
                </Typography>
                <Button
                    size="small"
                    aria-label="로그보기"
                    onClick={() => {
                        getLog("system");
                    }}
                >
                    <FormatListBulletedIcon />
                </Button>
            </Box>
            <Grid
                container
                spacing={2}
                columns={12}
                sx={{ mb: (theme) => theme.spacing(2) }}
            >
                {system.map((systemInfo, index) => (
                    <Grid size={{ xs: 12, sm: 6, lg: 3 }}>
                        <StatCard {...systemInfo} key={index} />
                    </Grid>
                ))}
                {/* <Grid size={{ sm: 12, md: 12 }}>
                    <SystemChart />
                </Grid> */}
            </Grid>
            <Grid
                container
                spacing={2}
                columns={12}
                sx={{ mb: (theme) => theme.spacing(2) }}
            >
                <Grid size={{ md: 12, lg: 6 }}>
                    <Box
                        sx={{
                            display: "flex",
                            alignItems: "center",
                            justifyContent: "space-between",
                            mb: 2,
                        }}
                    >
                        <Typography
                            component="h2"
                            variant="h6"
                            onClick={() => {
                                getLog("container");
                            }}
                        >
                            컨테이너{" "}
                            <Chip
                                size="medium"
                                color={
                                    containerStatus === "정상"
                                        ? "success"
                                        : "error"
                                }
                                label={containerStatus}
                            />
                        </Typography>
                        <Button
                            size="small"
                            aria-label="로그보기"
                            onClick={() => {
                                getLog("container");
                            }}
                        >
                            <FormatListBulletedIcon />
                        </Button>
                    </Box>
                    <ContainerDataGrid data={container} />
                </Grid>
                <Grid size={{ md: 12, lg: 6 }}>
                    <Box
                        sx={{
                            display: "flex",
                            alignItems: "center",
                            justifyContent: "space-between",
                            mb: 2,
                        }}
                    >
                        <Typography
                            component="h2"
                            variant="h6"
                            onClick={() => {
                                getLog("module");
                            }}
                        >
                            모듈{" "}
                            <Chip
                                size="medium"
                                color={
                                    moduleStatus === "정상"
                                        ? "success"
                                        : "error"
                                }
                                label={moduleStatus}
                            />
                        </Typography>
                        <Button
                            size="small"
                            aria-label="로그보기"
                            onClick={() => {
                                getLog("module");
                            }}
                        >
                            <FormatListBulletedIcon />
                        </Button>
                    </Box>
                    <ModuleDataGrid data={module} />
                </Grid>
                <Grid size={{ md: 12, lg: 12 }}>
                    <Box
                        sx={{
                            display: "flex",
                            alignItems: "center",
                            justifyContent: "space-between",
                            mb: 2,
                        }}
                    >
                        <Typography
                            component="h2"
                            variant="h6"
                            onClick={() => {
                                getLog("edgecam");
                            }}
                        >
                            엣지카메라{" "}
                            <Chip
                                size="medium"
                                color={
                                    edgecamStatus === "정상"
                                        ? "success"
                                        : "error"
                                }
                                label={edgecamStatus}
                            />
                        </Typography>
                        <Button
                            size="small"
                            aria-label="로그보기"
                            onClick={() => {
                                getLog("edgecam");
                            }}
                        >
                            <FormatListBulletedIcon />
                        </Button>
                    </Box>
                    <EdgecamDataGrid data={edgecam} />
                </Grid>
            </Grid>
            <Copyright sx={{ my: 4 }} />
            <LogDataGrid
                open={logTarget !== ""}
                close={() => {
                    getLog("");
                }}
                target={logTarget}
                data={log}
            />
        </Box>
    );
}
