import { useState, useEffect } from "react";
import Grid from "@mui/material/Grid2";
import Box from "@mui/material/Box";
import Chip from "@mui/material/Chip";
import Typography from "@mui/material/Typography";
import Copyright from "../internals/components/Copyright";
import SystemChart from "./SystemChart";
import StatCard from "./StatCard";
import ContainerDataGrid from "./ContainerDataGrid";
import ModuleDataGrid from "./ModuelDataGrid";
import EdgecamDataGrid from "./EdgecamDataGrid";
import axios from "axios";

export default function MainGrid() {
    const [updatedAt, setUpdatedAt] = useState(new Date());
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
    const [container, setContainer] = useState({
        status: "",
        web: false,
        was: false,
        module: false,
        mysql: false,
        redis: false,
    });
    const [module, setModule] = useState({
        status: "",
        process: 0,
        falldown: false,
        longterm: false,
        selfharm: false,
        emotion: false,
        violence: false,
    });
    const [edgecam, setEdgecam] = useState([]);

    const getData = async () => {
        const response = await axios.get("http://localhost:8000/live");
        const data = response["data"];
        setSystemData(data["system"]);
        setContainerData(data["container"]);
        setModuleData(data["module"]);
        setEdgecamData(data["edgecam"]);
        setUpdatedAt(new Date());
    };

    const setSystemData = (systemData) => {
        setSystemStatus(systemData["status"]);
        let pre = system;
        pre[0]["value"] = `${systemData["cpu"]}% 사용중`;
        pre[0]["gap"] = systemData["cpu"] - pre[0]["percent"];
        pre[0]["percent"] = systemData["cpu"];
        if (systemData["gpu"] === -1) {
            pre[1]["value"] = `사용할 수 없음`;
        } else {
            pre[1]["value"] = `${systemData["gpu"]}% 사용중`;
            pre[1]["gap"] = systemData["gpu"] - pre[1]["percent"];
            pre[1]["percent"] = systemData["gpu"];
        }
        pre[2]["value"] = `${systemData["memory"]}% 사용중`;
        pre[2]["gap"] = systemData["memory"] - pre[2]["percent"];
        pre[2]["percent"] = systemData["memory"];
        pre[3]["value"] = `${systemData["storage"]}% 사용중`;
        pre[3]["gap"] = systemData["storage"] - pre[3]["percent"];
        pre[3]["percent"] = systemData["storage"];
        pre = systemGraphHandler(pre, systemData);
        setSystem(pre);
    };

    const systemGraphHandler = (pre, cur) => {
        pre[0]["data"].push(cur["cpu"]);
        pre[1]["data"].push(cur["gpu"]);
        pre[2]["data"].push(cur["memory"]);
        pre[3]["data"].push(cur["storage"]);
        for (let i = 0; i < 4; i++) {
            if (pre[i]["data"].length > 30) {
                pre[i]["data"].shift();
            }
        }
        return pre;
    };

    const setContainerData = (containerData) => {
        setConatinerStatus(containerData["status"]);
        setContainer({
            status: containerData["status"],
            web: containerData["web"],
            was: containerData["was"],
            module: containerData["module"],
            mysql: containerData["mysql"],
            redis: containerData["redis"],
        });
    };

    const setModuleData = (moduleData) => {
        setModuleStatus(moduleData["status"]);
        setModule({
            status: moduleData["status"],
            process: moduleData["process"],
            falldown: moduleData["falldown"],
            longterm: moduleData["longterm"],
            selfharm: moduleData["selfharm"],
            emotion: moduleData["emotion"],
            violence: moduleData["violence"],
        });
    };
    const setEdgecamData = (edgecamData) => {
        setModuleStatus(edgecamData["status"]);
        let temp = [];
        edgecamData["edgecam"].forEach((item, idx) => {
            temp.push({
                id: idx,
                name: item["name"],
                camera:
                    item["camera"] === true
                        ? "Online"
                        : item["camera"] === null
                        ? "None"
                        : "Offlien",
                thermal:
                    item["thermal"] === true
                        ? "Online"
                        : item["thermal"] === null
                        ? "None"
                        : "Offlien",
                rader:
                    item["rader"] === true
                        ? "Online"
                        : item["rader"] === null
                        ? "None"
                        : "Offlien",
                toilet_rader:
                    item["toilet_rader"] === true
                        ? "Online"
                        : item["toilet_rader"] === null
                        ? "None"
                        : "Offlien",
            });
        });
        setEdgecam(temp);
    };

    useEffect(() => {
        const timer = setInterval(() => {
            getData();
        }, 3000);
        return () => clearInterval(timer);
    }, []);
    return (
        <Box sx={{ width: "100%", maxWidth: { sm: "100%", md: "1700px" } }}>
            {/* cards */}
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
                {system.map((card, index) => (
                    <Grid
                        key={updatedAt + index}
                        size={{ xs: 12, sm: 6, lg: 3 }}
                    >
                        <StatCard {...card} />
                    </Grid>
                ))}
                <Grid size={{ sm: 12, md: 12 }}>
                    <SystemChart />
                </Grid>
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
                    <ContainerDataGrid data={container} key={updatedAt} />
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
                    <ModuleDataGrid data={module} key={updatedAt} />
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
                    <EdgecamDataGrid data={edgecam} key={updatedAt} />
                </Grid>
            </Grid>
            <Copyright sx={{ my: 4 }} />
        </Box>
    );
}
