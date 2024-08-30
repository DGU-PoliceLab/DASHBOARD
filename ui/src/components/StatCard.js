import * as React from "react";
import PropTypes from "prop-types";
import { useTheme } from "@mui/material/styles";
import Box from "@mui/material/Box";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Chip from "@mui/material/Chip";
import Stack from "@mui/material/Stack";
import Typography from "@mui/material/Typography";
import { SparkLineChart } from "@mui/x-charts/SparkLineChart";
import { areaElementClasses } from "@mui/x-charts/LineChart";

function getDaysInMonth(month, year) {
    const date = new Date(year, month, 0);
    const monthName = date.toLocaleDateString("en-US", {
        month: "short",
    });
    const daysInMonth = date.getDate();
    const days = [];
    let i = 1;
    while (days.length < daysInMonth) {
        days.push(`${monthName} ${i}`);
        i += 1;
    }
    return days;
}

function AreaGradient({ color, id }) {
    return (
        <defs>
            <linearGradient id={id} x1="50%" y1="0%" x2="50%" y2="100%">
                <stop offset="0%" stopColor={color} stopOpacity={0.3} />
                <stop offset="100%" stopColor={color} stopOpacity={0} />
            </linearGradient>
        </defs>
    );
}

AreaGradient.propTypes = {
    color: PropTypes.string.isRequired,
    id: PropTypes.string.isRequired,
};

function StatCard({ title, value, interval, data, percent, gap }) {
    const theme = useTheme();
    const daysInWeek = getDaysInMonth(4, 2024);

    const trendColors = {
        normal:
            theme.palette.mode === "light"
                ? theme.palette.grey[400]
                : theme.palette.grey[500],
        error:
            theme.palette.mode === "light"
                ? theme.palette.error.main
                : theme.palette.error.dark,
    };

    const labelColors = {
        up: "success",
        down: "error",
        neutral: "default",
    };
    let trend = "neutral";
    const gapPoint = gap.toFixed(1);
    if (gapPoint > 0) {
        trend = "up";
    } else if (gapPoint < 0) {
        trend = "down";
    }
    const color = labelColors[trend];
    const flag = percent >= 95 ? "error" : "normal";
    const chartColor = trendColors[flag];

    return (
        <Card variant="outlined" sx={{ height: "100%", flexGrow: 1 }}>
            <CardContent>
                <Typography component="h2" variant="subtitle2" gutterBottom>
                    {title}
                </Typography>
                <Stack
                    direction="column"
                    sx={{
                        justifyContent: "space-between",
                        flexGrow: "1",
                        gap: 1,
                    }}
                >
                    <Stack sx={{ justifyContent: "space-between" }}>
                        <Stack
                            direction="row"
                            sx={{
                                justifyContent: "space-between",
                                alignItems: "center",
                            }}
                        >
                            <Typography variant="h4" component="p">
                                {value}
                            </Typography>
                            <Chip
                                size="small"
                                color={color}
                                label={
                                    gapPoint > 0
                                        ? `+${gapPoint}%`
                                        : `${gapPoint}%`
                                }
                            />
                        </Stack>
                        <Typography
                            variant="caption"
                            sx={{ color: "text.secondary" }}
                        >
                            실시간 사용률
                        </Typography>
                    </Stack>
                    <Box sx={{ width: "100%", height: 50 }}>
                        <SparkLineChart
                            colors={[chartColor]}
                            data={data}
                            area
                            showHighlight
                            showTooltip
                            xAxis={{
                                scaleType: "band",
                                data: daysInWeek, // Use the correct property 'data' for xAxis
                            }}
                            sx={{
                                [`& .${areaElementClasses.root}`]: {
                                    fill: `url(#area-gradient-${value})`,
                                },
                            }}
                        >
                            <AreaGradient
                                color={percent >= 90 ? "error" : "default"}
                                id={`area-gradient-${value}`}
                            />
                        </SparkLineChart>
                    </Box>
                </Stack>
            </CardContent>
        </Card>
    );
}

StatCard.propTypes = {
    data: PropTypes.arrayOf(PropTypes.number).isRequired,
    interval: PropTypes.string.isRequired,
    title: PropTypes.string.isRequired,
    trend: PropTypes.oneOf(["down", "neutral", "up"]).isRequired,
    value: PropTypes.string.isRequired,
};

export default StatCard;
