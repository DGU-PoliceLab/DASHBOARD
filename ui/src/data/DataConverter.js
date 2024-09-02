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
        console.log("PRE");
        console.table(result);
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

export const convContainerData = (data) => {
    let result = [
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
    ];
    return result;
};

export const convModuleData = (data) => {
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
