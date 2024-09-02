import { useState, useEffect } from "react";
import Grid from "@mui/material/Grid2";
import Box from "@mui/material/Box";
import Chip from "@mui/material/Chip";
import Typography from "@mui/material/Typography";
import Copyright from "../internals/components/Copyright";
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
} from "../data/DataConverter";

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
    const getData = async () => {
        const response = await axios.get("http://localhost:8000/live");
        const data = response["data"];
        setSystemData(data["system"]);
        setContainerData(data["container"]);
        setModuleData(data["module"]);
        setEdgecamData(data["edgecam"]);
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
            <Typography component="h2" variant="h6" sx={{ mb: 2 }}>
                시스템{" "}
                <Chip
                    size="medium"
                    color={systemStatus === "정상" ? "success" : "error"}
                    label={systemStatus}
                />
            </Typography>
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
                    <Typography component="h2" variant="h6" sx={{ mb: 2 }}>
                        컨테이너{" "}
                        <Chip
                            size="medium"
                            color={
                                containerStatus === "정상" ? "success" : "error"
                            }
                            label={containerStatus}
                        />
                    </Typography>
                    <ContainerDataGrid data={container} />
                </Grid>
                <Grid size={{ md: 12, lg: 6 }}>
                    <Typography component="h2" variant="h6" sx={{ mb: 2 }}>
                        모듈{" "}
                        <Chip
                            size="medium"
                            color={
                                moduleStatus === "정상" ? "success" : "error"
                            }
                            label={moduleStatus}
                        />
                    </Typography>
                    <ModuleDataGrid data={module} />
                </Grid>
                <Grid size={{ md: 12, lg: 12 }}>
                    <Typography component="h2" variant="h6" sx={{ mb: 2 }}>
                        엣지카메라{" "}
                        <Chip
                            size="medium"
                            color={
                                edgecamStatus === "정상" ? "success" : "error"
                            }
                            label={edgecamStatus}
                        />
                    </Typography>
                    <EdgecamDataGrid data={edgecam} />
                </Grid>
            </Grid>
            <Copyright sx={{ my: 4 }} />
        </Box>
    );
}
