export class GraphSeries {
    name: string | undefined;
    value: number | undefined;
    min: number | undefined;
    max: number | undefined;
}

export class GraphHeader {
    name: string | undefined;
    series: GraphSeries[] | undefined;
}

// Ngx chart properties
export class ChartProperties {
    view: [number, number] | undefined;
}