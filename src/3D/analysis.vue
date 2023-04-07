<template>
    <br><br>
    <el-row>
      <el-col :span="8">
        <el-tooltip content="预计时长：半分钟" placement="bottom" effect="light">
          <el-button class="button" @click="handleclick" round type="primary" :loading="loadone">分析</el-button>
        </el-tooltip>
      </el-col>
      <!--p style="color:cornflowerblue">"健康程度"仅供参考，请以医生建议为准</p-->
      <p style="color:cornflowerblue">默认选择推理后的结果，您也可以：</p>
        <el-upload
          class="buttonn"
          :on-change="handleChange"
          multiple
          :auto-upload="false"
          :limit="1"
        >
            <el-button  type="primary" :loading="loadtwo">选择本地文件</el-button>
      </el-upload>
    </el-row>
    <br>

    <!--el-col :span="10"-->
    <el-table
    class="Table"
    :data="tableData"
    :key="certin"
    style="width: 70%"
    @row-click="editCurrentApplicationApproval"
  >
    <el-table-column prop="name" label="器官"  width="100" />
      <!-- eslint-disable-next-line-->
      <!--template slot-scope="scope">
        <a @click="" style="color:blue;cursor:pointer">{{scope.row}}</a>
      </template-->
    <el-table-column prop="id" label="标签值" width="100"  sortable/>
    <el-table-column prop="num" label="体积" width="150" sortable />
    <el-table-column prop="Xlen" label="直径(X)" width="100" sortable />
    <el-table-column prop="Ylen" label="直径(Y)" width="100" sortable />
    <el-table-column prop="Zlen" label="直径(Z)" width="100" sortable />
    <el-table-column prop="XS" label="横截面(X)" width="120" sortable />
    <el-table-column prop="YS" label="横截面(Y)" width="120" sortable />
    <el-table-column prop="ZS" label="横截面(Z)" width="120" sortable />
    <el-table-column prop="p" label="健康程度（仅供参考）" width="200" sortable/>
  </el-table>
  <!--/el-col-->
  <!--el-col :span="2"></el-col>
  <el-col :span="8">
    <div  class="border" style="border:dashed;border-radius: 4px; box-shadow: 12px 12px 12px rgba(0,0,0,0.1);border-width: thin">
        <div v-show="shownum==='无'"><p>等待数据...</p></div>
        <div v-show="shownum==='脾脏'"><p>1</p></div>
        <div v-show="shownum==='胆囊'"><p>2</p></div>
    </div>
  </el-col-->
  <!--div  class="border" style="border:dashed;border-radius: 4px; box-shadow: 12px 12px 12px rgba(0,0,0,0.1);border-width: thin">
    <div v-show="shownum==='无'"><p>等待数据...</p></div>
    <div v-show="shownum==='脾脏'"><p>脾脏是一个位于左上腹部的器官，它有助于身体对红血球进行过滤和分解，同时也是免疫系统的一部分，负责产生和储存淋巴细胞和抗体。常见的脾脏疾病包括脾梗死、脾功能亢进、脾肿大等。</p></div>
    <div v-show="shownum==='胆囊'"><p>胆囊是一个位于肝脏下方的小囊状器官，主要功能是储存由肝脏产生的胆汁，当身体需要时，胆囊会将胆汁释放到小肠中，帮助消化脂肪。常见的胆囊疾病包括胆囊结石、胆囊炎、胆囊切除术等。</p></div>
    <div v-show="shownum==='右肾'"><p>肾脏是人体内最重要的器官之一，主要功能是过滤血液，排除废物和过多的水分，并产生尿液。右肾和左肾位于腹腔内两侧，右肾比左肾略低，两者大小和功能相似。常见的肾脏疾病包括肾结石、肾囊肿、肾炎、肾衰竭等。</p></div>
    <div v-show="shownum==='左肾'"><p>肾脏是人体内最重要的器官之一，主要功能是过滤血液，排除废物和过多的水分，并产生尿液。右肾和左肾位于腹腔内两侧，右肾比左肾略低，两者大小和功能相似。常见的肾脏疾病包括肾结石、肾囊肿、肾炎、肾衰竭等。</p></div>
    <div v-show="shownum==='食管'"><p>食管是一条管状结构，连接口腔和胃，负责将食物运输到胃中。常见的食管疾病包括食管癌、食管炎、食管溃疡等。</p></div>
    <div v-show="shownum==='肝脏'"><p>肝脏是人体内最大的内脏器官之一，负责合成胆汁、代谢药物和毒素、储存能量等。常见的肝脏疾病包括肝炎、肝硬化、脂肪肝等。</p></div>
    <div v-show="shownum==='胃'"><p>胃是一个位于腹部的J形器官，主要功能是消化食物。常见的胃部疾病包括胃溃疡、胃癌、胃炎等。</p></div>
    <div v-show="shownum==='主动脉'"><p>主动脉和下腔动脉是人体内两条最大的血管，分别负责将氧和营养物质输送到全身组织和器官。常见的动脉疾病包括动脉硬化、动脉瘤、动脉闭塞等。</p></div>
    <div v-show="shownum==='下腔动脉'"><p>主动脉和下腔动脉是人体内两条最大的血管，分别负责将氧和营养物质输送到全身组织和器官。常见的动脉疾病包括动脉硬化、动脉瘤、动脉闭塞等。</p></div>
    <div v-show="shownum==='胰腺'"><p>胰腺是一个位于腹部的长形腺体，主要功能是产生胰液和激素，帮助消化食物和调节血糖水平。常见的胰腺疾病包括胰腺炎、胰腺癌等。</p></div>
    <div v-show="shownum==='右肾上腺'"><p>肾上腺是一对小腺体，位于肾脏上方，主要分泌肾上腺素和去甲肾上腺素，调节身体的代谢和应激反应。常见的肾上腺疾病包括肾上腺功能亢进症、肾上腺皮质功能减退症等。</p></div>
    <div v-show="shownum==='左肾上腺'"><p>肾上腺是一对小腺体，位于肾脏上方，主要分泌肾上腺素和去甲肾上腺素，调节身体的代谢和应激反应。常见的肾上腺疾病包括肾上腺功能亢进症、肾上腺皮质功能减退症等。</p></div>
    <div v-show="shownum==='十二指肠'"><p>十二指肠是一段位于胃和小肠之间的结肠，主要功能是将胆汁和胰液分泌到小肠中，帮助消化和吸收营养。常见的十二指肠疾病包括十二指肠溃疡、十二指肠癌等。</p></div>
    <div v-show="shownum==='膀胱'"><p>膀胱是一个储存尿液的器官，位于盆腔底部。常见的膀胱疾病包括膀胱炎、膀胱结石、膀胱癌等。膀胱的正常功能需要神经、肌肉和泌尿系统的协调工作。</p></div>
    <div v-show="shownum==='前列腺/子宫'"><p>前列腺是男性生殖系统的一部分，位于膀胱下方，主要分泌前列腺液，帮助维持精液的液态。常见的前列腺疾病包括前列腺炎、前列腺增生、前列腺癌等。子宫是女性生殖系统的一部分，位于盆腔内，主要功能是容纳和孕育胎儿。常见的子宫疾病包括子宫肌瘤、子宫内膜异位症、子宫癌等。子宫还参与了月经周期的调节和生殖激素的代谢。</p></div>
  </div-->
  <el-card class="box-card">
    <template #header>
      <div class="card-header">
        <span>{{shownum}}</span>
      </div>
    </template>
    <div v-show="shownum==='器官名称'"><p>请点击表格查看</p></div>
    <div v-show="shownum==='脾脏'"><p>&nbsp&nbsp&nbsp&nbsp脾脏是一个位于左上腹部的器官，它有助于身体对红血球进行过滤和分解，同时也是免疫系统的一部分，负责产生和储存淋巴细胞和抗体，常见的脾脏疾病包括脾梗死、脾功能亢进、脾肿大等。<br>&nbsp&nbsp&nbsp&nbsp脾是重要的淋巴器官，位于腹腔的左上方，呈扁椭圆形，暗红色、质软而脆，当局部受暴力打击易破裂出血。脾位于左季肋区胃底与膈之间，恰与第9-11肋相对，其长轴与第10肋一致。正常情况下，左肋弓下缘不能触及。脾分为内、外两面，上、下两缘，前、后两端。内面凹陷与胃底、左肾、左肾上腺、胰尾和结肠左曲为邻，称为脏面。脏面近中央处有一条沟，是神经、血管出入之处，称脾门。外面平滑而隆凸与膈相对，称为膈面。上缘前部有2-3个切迹，称脾切迹。脾肿大时，脾切迹仍存在可作为触诊的标志。在脾附近，胃脾韧带及大网膜中，常可见到暗红色，大小不等，数目不一的副脾。因脾功能亢进作脾切除时，应将副脾一并切除。脾属于网状皮系统，是人体最大的淋巴器官，其结构基本上与淋巴结相似，由被膜、小梁及淋巴组织构成。其与淋巴结不同的地方是没有淋巴窦，但其中具有大量血窦。</p></div>
    <div v-show="shownum==='胆囊'"><p>&nbsp&nbsp&nbsp&nbsp胆囊是一个位于肝脏下方的小囊状器官，主要功能是储存由肝脏产生的胆汁，当身体需要时，胆囊会将胆汁释放到小肠中，帮助消化脂肪。常见的胆囊疾病包括胆囊结石、胆囊炎、胆囊切除术等。<br>&nbsp&nbsp&nbsp&nbsp胆囊，是位于右方肋骨下肝脏后方的梨形囊袋构造（肝的胆囊窝内），有浓缩和储存胆汁之作用。胆囊分底、体、颈、管四部，颈部连胆囊管。胆囊壁由粘膜、肌层和外膜三层组成。</p></div>
    <div v-show="shownum==='右肾'"><p>&nbsp&nbsp&nbsp&nbsp肾脏是人体内最重要的器官之一，主要功能是过滤血液，排除废物和过多的水分，并产生尿液。右肾和左肾位于腹腔内两侧，右肾比左肾略低，两者大小和功能相似。常见的肾脏疾病包括肾结石、肾囊肿、肾炎、肾衰竭等。<br>&nbsp&nbsp&nbsp&nbsp肾脏是人体泌尿系统中最重要的器官，在血液循环系统中，承担着滤过代谢废物并排出体外及重吸收各种营养物质的重要使命！肾脏位于人体腹腔后上部，脊椎两旁各有一个，受肝脏影响，右肾一般比左肾略低1-2厘米。除了肾脏以外，泌尿系统还包括输尿管、膀胱及尿道组成，泌尿系统的主要功能为排泄。
肾脏形似放大版的蚕豆，每一个肾的重量大概在100—200克，质柔软，是一个实质性的器官。肾脏皮质呈红褐色，分为外缘和内缘两部分，肾外缘为凸面，内缘为凹面，凹面中部为肾门，所有血管、神经及淋巴管均由此进入肾脏，肾盂则由此走出肾外。
肾单位是组成肾脏的结构和功能的基本单位，包括肾小体和肾小管。每个肾脏约有一百多万个肾单位，肾单位是肾脏部位物质交换和能量传输的重要系统，包括肾小球滤过血液形成原尿和肾小管、集合管重吸收营养物质及其毛细血管物质交换过程。因此，肾单位是肾脏微循环系统发挥作用的基本单位，对肾脏各功能的的正常运转起着决定性作用。</p></div>
    <div v-show="shownum==='左肾'"><p>&nbsp&nbsp&nbsp&nbsp肾脏是人体内最重要的器官之一，主要功能是过滤血液，排除废物和过多的水分，并产生尿液。右肾和左肾位于腹腔内两侧，右肾比左肾略低，两者大小和功能相似。常见的肾脏疾病包括肾结石、肾囊肿、肾炎、肾衰竭等。<br>&nbsp&nbsp&nbsp&nbsp肾脏是人体泌尿系统中最重要的器官，在血液循环系统中，承担着滤过代谢废物并排出体外及重吸收各种营养物质的重要使命！肾脏位于人体腹腔后上部，脊椎两旁各有一个，受肝脏影响，右肾一般比左肾略低1-2厘米。除了肾脏以外，泌尿系统还包括输尿管、膀胱及尿道组成，泌尿系统的主要功能为排泄。
肾脏形似放大版的蚕豆，每一个肾的重量大概在100—200克，质柔软，是一个实质性的器官。肾脏皮质呈红褐色，分为外缘和内缘两部分，肾外缘为凸面，内缘为凹面，凹面中部为肾门，所有血管、神经及淋巴管均由此进入肾脏，肾盂则由此走出肾外。
肾单位是组成肾脏的结构和功能的基本单位，包括肾小体和肾小管。每个肾脏约有一百多万个肾单位，肾单位是肾脏部位物质交换和能量传输的重要系统，包括肾小球滤过血液形成原尿和肾小管、集合管重吸收营养物质及其毛细血管物质交换过程。因此，肾单位是肾脏微循环系统发挥作用的基本单位，对肾脏各功能的的正常运转起着决定性作用。</p></div>
    <div v-show="shownum==='食管'"><p>&nbsp&nbsp&nbsp&nbsp食管是一条管状结构，连接口腔和胃，负责将食物运输到胃中。常见的食管疾病包括食管癌、食管炎、食管溃疡等。<br>&nbsp&nbsp&nbsp&nbsp食管是消化管道的一部分，上连于咽，沿脊柱椎体下行，穿过膈肌的食管裂孔通入胃，全长约25厘米。依食管的行程可将其分为颈部、胸部和腹部三段。食管主要由环节肌层(内层)和纵行肌层(外层)组成。由于这两种肌肉的收缩蠕动，迫使食物进入胃，故其主要作用是向胃内推进食物。</p></div>
    <div v-show="shownum==='肝脏'"><p>&nbsp&nbsp&nbsp&nbsp肝脏是人体内最大的内脏器官之一，负责合成胆汁、代谢药物和毒素、储存能量等。常见的肝脏疾病包括肝炎、肝硬化、脂肪肝等。<br>&nbsp&nbsp&nbsp&nbsp肝脏是身体内以代谢功能为主的一个器官，并在身体里面扮演着去氧化，储存肝糖，分泌性蛋白质的合成等等。肝脏也制造消化系统中之胆汁。肝脏是人体内脏里最大的器官，位于人体中的腹部位置，在右侧横隔膜之下，位于胆囊之前端且于右边肾脏的前方，胃的上方。肝脏是人体消化系统中最大的消化腺，为一红棕色的V 字形器官。</p></div>
    <div v-show="shownum==='胃'"><p>&nbsp&nbsp&nbsp&nbsp胃是一个位于腹部的J形器官，主要功能是消化食物。常见的胃部疾病包括胃溃疡、胃癌、胃炎等。<br>&nbsp&nbsp&nbsp&nbsp胃是人体的消化器官，位于膈下，上接食道，下通小肠。胃的上口为贲门，下口为幽门。故胃之上为食管，胃之下为肠管，胃居二者之间名为胃管（脘）。其分四部，贲门部、胃底、胃体和幽门部。</p></div>
    <div v-show="shownum==='主动脉'"><p>&nbsp&nbsp&nbsp&nbsp主动脉是人体内最大的血管，分别负责将氧和营养物质输送到全身组织和器官。常见的动脉疾病包括动脉硬化、动脉瘤、动脉闭塞等。<br>&nbsp&nbsp&nbsp&nbsp主动脉是人体内最粗大的动脉血管，是从心脏发出的向全身各部输送血液的主要导管，被称作生命的“拐杖”，包括胸主动脉和腹主动脉。人体内给心脏和大脑供血的血管叫中心血管，心、脑血管以外的主动脉分支血管则称作外周血管，分别供应胸腹盆腔脏器、以及躯干、四肢的血液。下面这张图比较直观，可以大致感受下。红色圈出来的就是主动脉，绿色圈出来的就是主要的外周血管部分。</p></div>
    <div v-show="shownum==='下腔静脉'"><p>&nbsp&nbsp&nbsp&nbsp下腔静脉体内最大的静脉干，为下腔静脉系的主干，在第5腰椎平面，由左、右髂总静脉合成，沿腹主动脉右侧上升，经肝的后方，穿膈的腔静脉孔入胸腔，进入右心房。收集下肢、盆腔和腹腔的静脉血。当下腔静脉阻塞时，在腹壁的两侧、脐平面以下可见到曲张血管。</p></div>
    <div v-show="shownum==='胰腺'"><p>&nbsp&nbsp&nbsp&nbsp胰腺是一个位于腹部的长形腺体，主要功能是产生胰液和激素，帮助消化食物和调节血糖水平。常见的胰腺疾病包括胰腺炎、胰腺癌等。<br>&nbsp&nbsp&nbsp&nbsp胰管位于胰实质内，其行状与胰的长轴一致，从胰尾经胰体走向胰头，沿途接受许多小叶间导管，最后于十二指肠降部的壁内与胆总管汇合成肝胰壶腹，开口于十二指肠大乳头。在胰头上部有时可见一小管，行于胰管上方，称为副胰管，开口于十二指肠小乳头。胰腺分为外分泌部和内分泌部两部分。外分泌腺由腺泡和腺管组成，腺泡分泌胰液，腺管是胰液排出的通道。胰液中含有碳酸氢钠、胰蛋白酶原、脂肪酶、淀粉酶等。胰液通过胰腺管排入十二指肠，有消化蛋白质、脂肪和糖的作用。</p></div>
    <div v-show="shownum==='右肾上腺'"><p>&nbsp&nbsp&nbsp&nbsp肾上腺是一对小腺体，位于肾脏上方，主要分泌肾上腺素和去甲肾上腺素，调节身体的代谢和应激反应。常见的肾上腺疾病包括肾上腺功能亢进症、肾上腺皮质功能减退症等。<br>&nbsp&nbsp&nbsp&nbsp肾上腺是人体相当重要的内分泌器官，由于位于两侧肾脏的上方，故名肾上腺。肾上腺左右各一，位于肾的上方，共同为肾筋膜和脂肪组织所包裹。左肾上腺呈半月形，右肾上腺为三角形。两侧共重10-15克。从侧面观察，腺体分肾上腺皮质和肾上腺髓质两部分，周围部分是皮质，内部是髓质。两者在发生、结构与功能上均不相同，实际上是两种内分泌腺。　</p></div>
    <div v-show="shownum==='左肾上腺'"><p>&nbsp&nbsp&nbsp&nbsp肾上腺是一对小腺体，位于肾脏上方，主要分泌肾上腺素和去甲肾上腺素，调节身体的代谢和应激反应。常见的肾上腺疾病包括肾上腺功能亢进症、肾上腺皮质功能减退症等。<br>&nbsp&nbsp&nbsp&nbsp肾上腺是人体相当重要的内分泌器官，由于位于两侧肾脏的上方，故名肾上腺。肾上腺左右各一，位于肾的上方，共同为肾筋膜和脂肪组织所包裹。左肾上腺呈半月形，右肾上腺为三角形。两侧共重10-15克。从侧面观察，腺体分肾上腺皮质和肾上腺髓质两部分，周围部分是皮质，内部是髓质。两者在发生、结构与功能上均不相同，实际上是两种内分泌腺。　</p></div>
    <div v-show="shownum==='十二指肠'"><p>&nbsp&nbsp&nbsp&nbsp十二指肠是一段位于胃和小肠之间的结肠，主要功能是将胆汁和胰液分泌到小肠中，帮助消化和吸收营养。常见的十二指肠疾病包括十二指肠溃疡、十二指肠癌等。<br>&nbsp&nbsp&nbsp&nbsp十二指肠为小肠的第一段，介于胃与空肠之间，由于相当于十二个横指并列的长度而得名，全长约25cm。十二指肠是小肠中长度最短、管径最大、位置最深且最为固定的部分。十二指肠除始、末两端被腹膜包裹，较为活动之外，其余大部分均为腹膜外位器官，被腹膜覆盖而固定于腹后壁。因为它既接受胃液，又接受胰液和胆汁，所以十二指肠的消化功能十分重要。十二指肠整体上呈“C”形，包绕胰头，可分为上部、降部、水平部和升部。</p></div>
    <div v-show="shownum==='膀胱'"><p>&nbsp&nbsp&nbsp&nbsp膀胱是一个储存尿液的器官，位于盆腔底部。常见的膀胱疾病包括膀胱炎、膀胱结石、膀胱癌等。膀胱的正常功能需要神经、肌肉和泌尿系统的协调工作。<br>&nbsp&nbsp&nbsp&nbsp是储存尿液的肌性囊状器官，其形状、大小、位置和壁的厚度随尿液充盈程度而异。通常成人的膀胱容量平均为350-500毫升，超过500毫升时候，因膀胱壁张力过大而产生疼痛。膀胱的最大容量为800毫升，新生儿的膀胱容量约为成人的十分之一，女性的容量小于男性，老年人因膀胱肌张力低而容量增大。</p></div>
    <div v-show="shownum==='前列腺/子宫'"><p>&nbsp&nbsp&nbsp&nbsp前列腺是男性生殖系统的一部分，位于膀胱下方，主要分泌前列腺液，帮助维持精液的液态。常见的前列腺疾病包括前列腺炎、前列腺增生、前列腺癌等。子宫是女性生殖系统的一部分，位于盆腔内，主要功能是容纳和孕育胎儿。常见的子宫疾病包括子宫肌瘤、子宫内膜异位症、子宫癌等。子宫还参与了月经周期的调节和生殖激素的代谢。</p></div>
  </el-card>
  <!--Multi></Multi-->
  <change></change>
</template>



<script lang="ts">
import axios from 'axios'
import type { TableColumnCtx } from 'element-plus'
import {ref}from 'vue'
import change from './change.vue'



export default{
  data()
  {
    return{
      certin:true,
      //tableData:[],
      shownum:'器官名称',
      tableData: [],
      fileList:[],
      loadone:false,
      loadtwo:false,
    }
  },
  components:{
    change,
  },
  methods:{
    handleclick()
    {
      this.loadone=true,
        axios.post("http://127.0.0.1:5000/analyse", 1).then(responce => {
          console.log(responce)
          this.tableData= responce.data
          console.log(this.tableData)
          this.loadone=false
          this.certin=!this.certin
        })
    },
    editCurrentApplicationApproval(row){
      this.shownum=row.name
      console.log(this.shownum)
    },

    handleChange(file, fileList)
    {
      this.loadtwo=true
      console.log(fileList)
      this.fileList = fileList;
      var param = new FormData();
      
					this.fileList.forEach(
						(val, index) => {
							param.append("file", val.raw);
						}
					);
          console.log(param)
					axios.post("http://127.0.0.1:5000/uploadan", param).then(responce => {
            console.log(responce)
            this.loadtwo=false
            this.tableData= responce.data
            this.certin=!this.certin
          });
    },
  }
}










</script>

<style scoped>
.button{
  transform: translate(10vw,0);
}
.buttonn
{
  transform: translate(-0vh,0);
}
.border
{
  background-color: mediumspringgreen;
  width: 60vw;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text {
  font-size: 14px;
}


.box-card {
  width: 1200px;
}
</style>