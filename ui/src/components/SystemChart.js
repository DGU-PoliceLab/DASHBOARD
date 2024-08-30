import * as React from "react";
import PropTypes from "prop-types";
import { useTheme } from "@mui/material/styles";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Chip from "@mui/material/Chip";
import Typography from "@mui/material/Typography";
import Stack from "@mui/material/Stack";
import { LineChart } from "@mui/x-charts/LineChart";

function AreaGradient({ color, id }) {
    return (
        <defs>
            <linearGradient id={id} x1="50%" y1="0%" x2="50%" y2="100%">
                <stop offset="0%" stopColor={color} stopOpacity={0.5} />
                <stop offset="100%" stopColor={color} stopOpacity={0} />
            </linearGradient>
        </defs>
    );
}

AreaGradient.propTypes = {
    color: PropTypes.string.isRequired,
    id: PropTypes.string.isRequired,
};

function getDaysInMonth(y, m, d) {
    const date = new Date(y, m - 1, d);
    let py = 0;
    let pm = 0;
    let pl = 0;
    if (m - 2 < 1) {
        py = y - 1;
        pm = m - 1;
    } else {
        py = y;
        pm = m - 1;
    }
    const preDate = new Date(py, pm, 0);
    pl = preDate.getDate();

    const monthName = date.toLocaleDateString("ko-KR", {
        month: "short",
    });
    const preMonthName = preDate.toLocaleDateString("ko-KR", {
        month: "short",
    });
    const days = [];
    let i = d;
    while (days.length < 30) {
        if (i < 1) {
            days.push(`${preMonthName} ${pl + i}일`);
        } else {
            days.push(`${monthName} ${i}일`);
        }
        i -= 1;
    }
    days.reverse();
    return days;
}

export default function SystemChart() {
    const theme = useTheme();
    const now = new Date();
    const data = getDaysInMonth(
        now.getFullYear(),
        now.getMonth() + 1,
        now.getDate()
    );

    const colorPalette = [
        theme.palette.primary.light,
        theme.palette.primary.main,
        theme.palette.primary.dark,
    ];

    return (
        <Card variant="outlined" sx={{ width: "100%" }}>
            <CardContent>
                <Typography component="h2" variant="subtitle2" gutterBottom>
                    시스템 로그
                </Typography>
                <Stack sx={{ justifyContent: "space-between" }}>
                    <Typography
                        variant="caption"
                        sx={{ color: "text.secondary" }}
                    >
                        지난 30일
                    </Typography>
                </Stack>
                <LineChart
                    colors={colorPalette}
                    xAxis={[
                        {
                            scaleType: "point",
                            data,
                            tickInterval: (index, i) => (i + 1) % 1 === 0,
                        },
                    ]}
                    series={[
                        {
                            id: "direct",
                            label: "최소",
                            showMark: false,
                            curve: "linear",
                            stack: "total",
                            area: true,
                            stackOrder: "ascending",
                            data: [10, 17, 12, 15, 14, 13, 12],
                        },
                        {
                            id: "referral",
                            label: "평균",
                            showMark: false,
                            curve: "linear",
                            stack: "total",
                            area: true,
                            stackOrder: "ascending",
                            data: [12, 15, 13, 12, 13, 15, 18],
                        },
                        {
                            id: "organic",
                            label: "최대",
                            showMark: false,
                            curve: "linear",
                            stack: "total",
                            stackOrder: "ascending",
                            data: [50, 53, 55, 52, 30, 70, 55],
                            area: true,
                        },
                    ]}
                    height={250}
                    margin={{ left: 50, right: 20, top: 20, bottom: 20 }}
                    grid={{ horizontal: true }}
                    sx={{
                        "& .MuiAreaElement-series-organic": {
                            fill: "url('#organic')",
                        },
                        "& .MuiAreaElement-series-referral": {
                            fill: "url('#referral')",
                        },
                        "& .MuiAreaElement-series-direct": {
                            fill: "url('#direct')",
                        },
                    }}
                    slotProps={{
                        legend: {
                            hidden: true,
                        },
                    }}
                >
                    <AreaGradient
                        color={theme.palette.primary.dark}
                        id="organic"
                    />
                    <AreaGradient
                        color={theme.palette.primary.main}
                        id="referral"
                    />
                    <AreaGradient
                        color={theme.palette.primary.light}
                        id="direct"
                    />
                </LineChart>
            </CardContent>
        </Card>
    );
}
