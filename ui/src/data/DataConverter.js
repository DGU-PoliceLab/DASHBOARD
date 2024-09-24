export const convSystemData = (data, pre) => {
    let result = {};
    if (pre.length === 0) {
        result = [
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
        ];
    } else {
        result = pre;
        result[0]["value"] = `${data["cpu"]}% 사용중`;
        result[0]["gap"] = data["cpu"] - pre[0]["percent"];
        result[0]["percent"] = data["cpu"];
        if (data["gpu"] === -1) {
            result[1]["value"] = `사용할 수 없음`;
        } else {
            result[1]["value"] = `${data["gpu"]}% 사용중`;
            result[1]["gap"] = data["gpu"] - pre[1]["percent"];
            result[1]["percent"] = data["gpu"];
        }
        result[2]["value"] = `${data["memory"]}% 사용중`;
        result[2]["gap"] = data["memory"] - pre[2]["percent"];
        result[2]["percent"] = data["memory"];
        result[3]["value"] = `${data["storage"]}% 사용중`;
        result[3]["gap"] = data["storage"] - pre[3]["percent"];
        result[3]["percent"] = data["storage"];
        result[0]["data"].push(data["cpu"]);
        result[1]["data"].push(data["gpu"]);
        result[2]["data"].push(data["memory"]);
        result[3]["data"].push(data["storage"]);
        for (let i = 0; i < 4; i++) {
            if (result[i]["data"].length > 30) {
                result[i]["data"].shift();
            }
        }
    }
    return result;
};

export const convSystemLog = (log) => {
    let result = [];
    log.forEach((item, idx) => {
        result.push({
            id: item[0],
            level: item[1],
            occurred_at: new Date(item[2] * 1000).toLocaleString(),
            cpu_usage: item[3],
            cpu_usage_core: item[4],
            gpu_usage_rate: item[5],
            gpu_mem_usage_rate: item[6],
            gpu_mem_usage: item[7],
            memory_usage_rate: item[8],
            memory_usage: (item[9] / 1024 / 1024).toFixed(2),
            storage_usage_rate: item[10],
            storage_usage: (item[11] / 1024 / 1024).toFixed(2),
        });
    });
    return result;
};

export const convContainerData = (data) => {
    let result = [
        {
            id: 1,
            name: "pls-platform",
            desc: "웹 서비스 구동을 위한 컨테이너",
            status: data["platform"] ? "Online" : "Offline",
        },
        {
            id: 2,
            name: "pls-module",
            desc: "인공지능 모듈 구동을 위한 컨테이너",
            status: data["module"] ? "Online" : "Offline",
        },
        {
            id: 3,
            name: "pls-mysql",
            desc: "기반 데이터 저장을 위한 컨테이너",
            status: data["mysql"] ? "Online" : "Offline",
        },
        {
            id: 4,
            name: "pls-redis",
            desc: "임시 및 캐싱 데이터 저장을 위한 컨테이너",
            status: data["redis"] ? "Online" : "Offline",
        },
        {
            id: 5,
            name: "-",
            desc: "-",
            status: "None",
        },
    ];
    return result;
};

export const convContainerLog = (log) => {
    let result = [];
    log.forEach((item, idx) => {
        result.push({
            id: item[0],
            level: item[1],
            occurred_at: new Date(item[2] * 1000).toLocaleString(),
            platform: item[3] === 1 ? "Online" : "Offline",
            module: item[4] === 1 ? "Online" : "Offline",
            mysql: item[5] === 1 ? "Online" : "Offline",
            redis: item[6] === 1 ? "Online" : "Offline",
            is_error: item[7] === 1 ? "True" : "False",
        });
    });
    return result;
};

export const convModuleData = (data) => {
    console.log(data);

    let result = [
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
    ];
    return result;
};

export const convModuleLog = (log) => {
    let result = [];
    log.forEach((item, idx) => {
        result.push({
            id: item[0],
            level: item[1],
            occurred_at: new Date(item[2] * 1000).toLocaleString(),
            process_fps: item[3],
            falldown: item[4] === 1 ? "Online" : "Offline",
            selfharm: item[5] === 1 ? "Online" : "Offline",
            emotion: item[6] === 1 ? "Online" : "Offline",
            violence: item[7] === 1 ? "Online" : "Offline",
            longterm: item[8] === 1 ? "Online" : "Offline",
            is_error: item[9] === 1 ? "True" : "False",
        });
    });
    return result;
};

export const convEdgecamData = (data) => {
    let result = [];
    data.forEach((item, idx) => {
        result.push({
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
    return result;
};

export const convEdgecamLog = (log) => {
    let result = [];
    log.forEach((item, idx) => {
        result.push({
            id: item[0],
            level: item[1],
            occurred_at: new Date(item[2] * 1000).toLocaleString(),
            edgecam: item[3],
            is_error: item[4] === 1 ? "True" : "False",
        });
    });
    return result;
};
