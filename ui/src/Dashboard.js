import * as React from "react";
import { createTheme, ThemeProvider, alpha } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import Box from "@mui/material/Box";
import Stack from "@mui/material/Stack";
import getDashboardTheme from "./theme/getDashboardTheme";
import AppNavbar from "./components/AppNavbar";
import Header from "./components/Header";
import MainGrid from "./components/MainGrid";
import TemplateFrame from "./TemplateFrame";

export default function Dashboard() {
    const [mode, setMode] = React.useState("dark");
    const [showCustomTheme, setShowCustomTheme] = React.useState(true);
    const dashboardTheme = createTheme(getDashboardTheme(mode));
    const defaultTheme = createTheme({ palette: { mode } });

    const toggleColorMode = () => {
        const newMode = mode === "dark" ? "light" : "dark";
        setMode(newMode);
        localStorage.setItem("themeMode", newMode); // Save the selected mode to localStorage
    };

    const toggleCustomTheme = () => {
        setShowCustomTheme((prev) => !prev);
    };

    return (
        <TemplateFrame
            toggleCustomTheme={toggleCustomTheme}
            showCustomTheme={showCustomTheme}
            mode={mode}
            toggleColorMode={toggleColorMode}
        >
            <ThemeProvider
                theme={showCustomTheme ? dashboardTheme : defaultTheme}
            >
                <CssBaseline enableColorScheme />
                <Box sx={{ display: "flex" }}>
                    <AppNavbar />
                    <Box
                        component="main"
                        sx={(theme) => ({
                            flexGrow: 1,
                            backgroundColor: alpha(
                                theme.palette.background.default,
                                1
                            ),
                            overflow: "auto",
                        })}
                    >
                        <Stack
                            spacing={2}
                            sx={{
                                alignItems: "center",
                                mx: 3,
                                pt: 2,
                                pb: 10,
                                mt: { xs: 8, md: 0 },
                            }}
                        >
                            <MainGrid />
                        </Stack>
                    </Box>
                </Box>
            </ThemeProvider>
        </TemplateFrame>
    );
}
