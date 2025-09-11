import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static class TestCase {
        final String desc; final String op; final String a; final String b;
        TestCase(String desc, String op, String a, String b) { this.desc = desc; this.op = op; this.a = a; this.b = b; }
    }

    public static void main(String[] args) throws IOException {
        List<TestCase> tests = new ArrayList<>();
        tests.add(new TestCase("加法测试", "add", "5", "3"));
        tests.add(new TestCase("减法测试", "subtract", "10", "4"));
        tests.add(new TestCase("乘法测试", "multiply", "7", "2"));
        tests.add(new TestCase("除法测试（正常）", "divide", "8", "2"));
        tests.add(new TestCase("除法测试（除零）", "divide", "5", "0"));
        tests.add(new TestCase("幂运算测试（正常）", "power", "2", "3"));
        tests.add(new TestCase("幂运算测试（异常）", "power", "-4", "0.5"));
        tests.add(new TestCase("类型错误测试", "add", "5a", "3"));
        tests.add(new TestCase("未知操作测试", "mod", "10", "3"));

        StringBuilder md = new StringBuilder();
        md.append("# 验证报告\n\n");
        md.append("| 用例 | 操作 | 输入(num1,num2) | 结果/异常 | 详情 |\n");
        md.append("|---|---|---|---|---|\n");

        for (TestCase t : tests) {
            String outcome;
            String detail;
            try {
                double a = Double.parseDouble(t.a);
                double b = Double.parseDouble(t.b);
                double res = Calculator.calculate(t.op, a, b);
                outcome = String.valueOf(res);
                detail = "成功";
            } catch (Exception e) {
                outcome = e.getClass().getSimpleName();
                detail = e.getMessage() == null ? "" : e.getMessage();
            }
            System.out.printf("%s: %s(%s,%s) -> %s %s\n", t.desc, t.op, t.a, t.b, outcome, detail.isEmpty()?"":"- "+detail);
            md.append(String.format("| %s | %s | (%s,%s) | %s | %s |\n", t.desc, t.op, t.a, t.b, outcome, detail.replace("|","\\|")));
        }

        Files.writeString(Path.of("report.md"), md.toString(), StandardCharsets.UTF_8);
        System.out.println("\n报告已生成: report.md");
    }
}
